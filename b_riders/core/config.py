from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Bike Rides"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///rides.db"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    API_V1_STR: str = "v1"
    SECRET_KEY: str = "change_this"
    BACKEND_CORS_ORIGINS: List[str] = []
    TEST_SUPERUSER: str = "teste@teste.com"
    TEST_SUPERUSER_PASSWORD: str = "teste"


settings = Settings()
