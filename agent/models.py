from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Literal, Type, Union
from pydantic import Field


class ActionName(str, Enum):
    """
    Enumeration of supported action names that can be performed by the agent.
    """
    GET_WEATHER = "get_weather"
    GET_NEWS = "get_news"


class ActionBase(BaseModel):
    """
    Base class for all actions with common properties.
    """
    action_name: ActionName


class GetWeatherParameters(BaseModel):
    """
    Parameters required for retrieving weather information.
    """
    city: str
    state_or_province: str
    country: str


class GetWeatherAction(ActionBase):
    """
    Action for retrieving weather data for a specified location.
    """
    action_name: Literal[ActionName.GET_WEATHER] = ActionName.GET_WEATHER
    parameters: GetWeatherParameters


class GetNewsParameters(BaseModel):
    """
    Parameters required for retrieving news information.
    """
    topic: str


class GetNewsAction(ActionBase):
    """
    Action for retrieving news articles about a specified topic.
    """
    action_name: Literal[ActionName.GET_NEWS] = ActionName.GET_NEWS
    parameters: GetNewsParameters


class GeoCodingResult(BaseModel):
    """
    Result from geocoding API containing location details.
    """
    name: str
    latitude: float
    longitude: float


class GeoCodingResponse(BaseModel):
    """
    Complete response from the geocoding API.
    """
    results: List[GeoCodingResult]
    generationtime_ms: float


class CurrentWeatherUnits(BaseModel):
    """
    Units of measurement for weather data.
    """
    time: str
    interval: str
    temperature_2m: str
    precipitation: str
    windspeed_10m: str


class CurrentWeatherConditions(BaseModel):
    """
    Current weather conditions with specific measurements.
    """
    time: str
    interval: int
    temperature_2m: float
    precipitation: float
    windspeed_10m: float


class WeatherResult(BaseModel):
    """
    Complete weather data returned from the weather API.
    """
    latitude: float
    longitude: float
    generationtime_ms: float
    utc_offset_seconds: int
    timezone: str
    timezone_abbreviation: str
    elevation: int
    current_units: CurrentWeatherUnits
    current: CurrentWeatherConditions


class ChatCompletionMessage(BaseModel):
    """
    Message format for interactions with the LLM.
    """
    role: str
    content: str


# Type definition for actions the system can perform
ActionType: Type[GetWeatherAction | GetNewsAction] = Union[GetWeatherAction, GetNewsAction]


class ThoughtAndActionModel(BaseModel):
    """
    Represents the AI's thought process and the action it proposes based on the user's input.
    """
    thought: str
    action: Optional[ActionType]


class NewsArticleSource(BaseModel):
    """
    Information about the source of a news article.
    """
    id: str | None
    name: str


class NewsArticle(BaseModel):
    """
    Detailed information about a news article.
    """
    source: NewsArticleSource
    author: str | None
    description: str
    url: str
    url_to_image: str = Field(alias="urlToImage")
    publishedAt: str
    content: str


class NewsResult(BaseModel):
    """
    Complete news data returned from the news API.
    """
    status: str
    total_results: int = Field(alias="totalResults")
    articles: list[NewsArticle]
