from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Literal, Type, Union
from pydantic import Field


class ActionName(str, Enum):
    GET_WEATHER = "get_weather"
    GET_NEWS = "get_news"


class ActionBase(BaseModel):
    action_name: ActionName


class GetWeatherParameters(BaseModel):
    city: str
    state_or_province: str
    country: str


class GetWeatherAction(ActionBase):
    action_name: Literal[ActionName.GET_WEATHER] = ActionName.GET_WEATHER
    parameters: GetWeatherParameters


class GetNewsParameters(BaseModel):
    topic: str


class GetNewsAction(ActionBase):
    action_name: Literal[ActionName.GET_NEWS] = ActionName.GET_NEWS
    parameters: GetNewsParameters


class GeoCodingResult(BaseModel):
    name: str
    latitude: float
    longitude: float


class GeoCodingResponse(BaseModel):
    results: List[GeoCodingResult]
    generationtime_ms: float


class CurrentWeatherUnits(BaseModel):
    time: str
    interval: str
    temperature_2m: str
    precipitation: str
    windspeed_10m: str


class CurrentWeatherConditions(BaseModel):
    time: str
    interval: int
    temperature_2m: float
    precipitation: float
    windspeed_10m: float


class WeatherResult(BaseModel):
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
    role: str
    content: str


ActionType: Type[GetWeatherAction | GetNewsAction] = Union[GetWeatherAction, GetNewsAction]


class ThoughtAndActionModel(BaseModel):
    """
    Represents the AI's thought process and the action it proposes based on the user's input.
    """
    thought: str
    action: Optional[ActionType]


class NewsArticleSource(BaseModel):
    id: str | None
    name: str


class NewsArticle(BaseModel):
    source: NewsArticleSource
    author: str | None
    description: str
    url: str
    url_to_image: str = Field(alias="urlToImage")
    publishedAt: str
    content: str


class NewsResult(BaseModel):
    status: str
    total_results: int = Field(alias="totalResults")
    articles: list[NewsArticle]
