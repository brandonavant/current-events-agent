from typing import List

from .models import ActionName, GetWeatherParameters, GetNewsParameters, GetWeatherAction, GetNewsAction, ActionType

AVAILABLE_ACTIONS: List[ActionType] = [
    GetWeatherAction(
        action_name=ActionName.GET_WEATHER,
        parameters=GetWeatherParameters(
            city="<the_requested_city>",
            state_or_province="<the_requested_state_or_province>",
            country="<the_requested_country>"
        )
    ),
    GetNewsAction(
        action_name=ActionName.GET_NEWS,
        parameters=GetNewsParameters(
            topic="<the_requested_topic>"
        )
    )
]