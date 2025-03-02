from openai import OpenAI
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger: logging.Logger = logging.getLogger(__name__)
llm_client = OpenAI()