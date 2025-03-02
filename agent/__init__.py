"""
Current Events Agent Package

A package that provides an intelligent agent capable of answering questions about 
current events by fetching real-time data from external APIs and processing 
user inquiries using natural language.
"""

from .config import Settings

from .models import (
    ActionName,
    ActionBase,
    GetWeatherParameters,
    GetNewsParameters,
    GetWeatherAction,
    GetNewsAction,
    GeoCodingResult,
    GeoCodingResponse,
    CurrentWeatherUnits,
    CurrentWeatherConditions,
    WeatherResult,
    NewsArticleSource,
    NewsArticle,
    NewsResult,
    ChatCompletionMessage,
    ThoughtAndActionModel,
)

__all__ = [
    "ActionName",
    "ActionBase",
    "GetWeatherParameters",
    "GetNewsParameters",
    "GetWeatherAction",
    "GetNewsAction",
    "GeoCodingResult",
    "GeoCodingResponse",
    "CurrentWeatherUnits",
    "CurrentWeatherConditions",
    "WeatherResult",
    "NewsArticleSource",
    "NewsArticle",
    "NewsResult",
    "ChatCompletionMessage",
    "ThoughtAndActionModel",
    "Settings",
]