import os

from pydantic_settings import BaseSettings
DOTENV = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.env"))


class Settings(BaseSettings):
    # Graphql

    # Database
    POSTGRES_HOSTNAME: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    class Config:
        env_file = DOTENV


settings = Settings()
