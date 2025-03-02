import requests
import datetime

from .models import (
    WeatherResult,
    NewsResult,
    GeoCodingResult,
    GeoCodingResponse,
    GetWeatherAction
)

from .config import settings


def get_weather(geo_info: GeoCodingResult) -> WeatherResult:
    url: str = (f"https://api.open-meteo.com/v1/forecast?latitude={geo_info.latitude}"
                f"&longitude={geo_info.longitude}"
                f"&current=temperature_2m,precipitation,windspeed_10m"
                f"&timezone=UTC")

    json_response = requests.request("GET", url)
    weather_response: WeatherResult = WeatherResult.model_validate(json_response.json())

    if not weather_response.current:
        raise ValueError(
            f"Call to Weather API did not yield a viable condition result for '{geo_info.latitude} lat'/'{geo_info.longitude}'."
        )

    return weather_response


def get_news(news_topic: str) -> NewsResult:
    from_yesterday: datetime = datetime.datetime.now() - datetime.timedelta(days=1)
    from_yesterday_formatted = from_yesterday.strftime("%Y-%m-%d")
    url: str = f"https://newsapi.org/v2/everything"

    params = {
        "q": news_topic,
        "from": from_yesterday_formatted,
        "sortBy": "popularity",
        "apiKey": settings.news_api_token,
        "pageSize": 4,
    }

    json_response = requests.request("GET", url, params=params)
    news_response = NewsResult.model_validate(json_response.json())

    return news_response


def get_geo_info(action: GetWeatherAction) -> GeoCodingResult:
    city: str = action.parameters.city
    state_or_province: str = action.parameters.state_or_province
    country: str = action.parameters.country
    url: str = (f'https://geocoding-api.open-meteo.com/v1/search?name={city}'
                f'&country={country}&admin1={state_or_province}'
                f'&count=1'
                f'&language=en'
                f'&format=json')

    json_response = requests.request("GET", url)
    geo_coding_response = GeoCodingResponse.model_validate(json_response.json())

    if not geo_coding_response.results:
        raise ValueError(
            f"Call to GeoCoding API did not yield a viable location for '{city},{state_or_province},{country}'"
        )

    return geo_coding_response.results[0]