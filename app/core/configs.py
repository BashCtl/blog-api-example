from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from pydantic import AnyHttpUrl


class Settings(BaseSettings):
    PROJECT_NAME: str
    DB_URI: str
    DB_NAME: str
    TEST_DB_NAME: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    API_VERSION: str
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    ALLOW_METHODS: List[str] = ["*"]
    ALLOW_HEADERS: List[str] = ["*"]

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
