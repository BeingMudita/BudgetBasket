from pydantic_settings import BaseSettings
from functools import lru_cache


from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    APP_ENV: str

    API_V1_PREFIX: str

    SECRET_KEY: str

    DATABASE_URL: str

    REDIS_HOST: str
    REDIS_PORT: int

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()