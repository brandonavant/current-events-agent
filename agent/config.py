from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Get the absolute path to the .env file
ENV_FILE = Path(__file__).parent.parent / ".env"

# Load environment variables first
load_dotenv(ENV_FILE)


class Settings(BaseSettings):
    """
    Defines application settings, which are pulled from the .env file.
    """
    openai_api_key: str
    news_api_token: str

    class Config:
        """
        Configuration which specifies that the settings are loaded from a .env file.
        """
        env_file = str(ENV_FILE)
        env_file_encoding = "utf-8"


settings = Settings()