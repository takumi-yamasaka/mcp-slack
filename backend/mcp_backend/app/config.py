import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./mcp.db")
    model_name: str = "gpt-4o"  # Default model, can be changed

    class Config:
        env_file = ".env"

settings = Settings()
