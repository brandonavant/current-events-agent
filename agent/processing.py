import json
import textwrap
import time

from pydantic import BaseModel, ValidationError
from .clients import get_news, get_weather, get_geo_info
from .common import llm_client, logger

from .constants import LLM_RETRY_DELAY_IN_SECONDS, LLM_ATTEMPT_LIMIT, SYSTEM_PROMPT, LLM_NAME
from .models import ThoughtAndActionModel, ActionName, GeoCodingResult, WeatherResult, NewsResult
from .actions import AVAILABLE_ACTIONS

def generate_thought_and_action(user_input: str) -> str:
    """
    Presents the user's original input to the LLM, which will construct a structured payload (JSON) containing its thoughts on the request and the action it thinks should be taken.
    :param user_input: The user's input.
    :return: A structured JSON payload containing the AI's thoughts and the action it proposes.
    """
    user_inquiry_prompt: str = textwrap.dedent(f"""
        Analyze the following user request and determine the next action that should be taken to fulfill their inquiry. The available actions are as follows:
        {json.dumps([action.model_dump() for action in AVAILABLE_ACTIONS], indent=2)}

        The user's input is as follows:
        {user_input}

        Please return a JSON object following this schema:
        {{
          "thought": "<your reasoning>",
          "action": {{
              "action_name": "<chosen_action_name>",
              "parameters": {{
                "<param1_name>": "<param1_value>",
                ...
            }}
          }}
        }}
        For the `thought`, please include your thought process around the user's request and the action that you've determine would be most appropriate.
        If the user’s request does not match any of the available actions, set `"action": null`. Your reasoning should explain that the inquiry is unsupported while keeping it relevant to the topic requested. Do not assume missing parameters for unrelated actions.
    """).strip()

    messages: list[dict[str, str]] = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_inquiry_prompt
        }
    ]

    llm_output = llm_client.chat.completions.create(model=LLM_NAME, messages=messages)

    return llm_output.choices[0].message.content


def process_user_inquiry(user_inquiry: str) -> ThoughtAndActionModel:
    for attempt in range(LLM_ATTEMPT_LIMIT):
        result = generate_thought_and_action(user_inquiry)
        try:
            return ThoughtAndActionModel.model_validate_json(result)
        except ValidationError as e:
            logger.error("Attempt %d failed", attempt + 1, exc_info=e)
            time.sleep(LLM_RETRY_DELAY_IN_SECONDS)

    raise RuntimeError("Failed to parse LLM response after multiple attempts.")


def generate_final_response(user_inquiry: str, thought_and_action: ThoughtAndActionModel, result: BaseModel) -> str:
    final_response_prompt: str = textwrap.dedent(f"""
        The user has made the following inquiry:
        {user_inquiry}

        From this inquiry, we came concluded the following:
        {thought_and_action.thought}

        We invoked the available action '{thought_and_action.action.action_name}' using the following parameters:
        {thought_and_action.action.model_dump_json()}

        We then received the following results:
        {result.model_dump_json()}

        Please provide for the user a conclusive analysis the results of their inquiry.
    """).strip()

    messages: list[dict[str, str]] = [
        {
            "role": "user",
            "content": final_response_prompt
        }
    ]

    llm_output = llm_client.chat.completions.create(model=LLM_NAME, messages=messages)

    return llm_output.choices[0].message.content


def invoke_action(user_inquiry: str, thought_and_action: ThoughtAndActionModel) -> str:
    if thought_and_action is None:
        raise RuntimeError("Encountered an unexpected error when calling LLM.")

    if thought_and_action.action is None:
        return thought_and_action.thought

    if thought_and_action.action.action_name == ActionName.GET_WEATHER:
        geo_info: GeoCodingResult = get_geo_info(thought_and_action.action)
        weather_result: WeatherResult = get_weather(geo_info)
        return generate_final_response(user_inquiry, thought_and_action, weather_result)
    elif thought_and_action.action.action_name == ActionName.GET_NEWS:
        news_result: NewsResult = get_news(thought_and_action.action.parameters.topic)
        return generate_final_response(user_inquiry, thought_and_action, news_result)
    else:
        raise RuntimeError("Unknown action")
