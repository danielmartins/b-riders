from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: Optional[str] = "sqlite:///rides.db"
    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[int] = 60


settings = Settings()
