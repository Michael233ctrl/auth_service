import os
import secrets
from typing import Any, Annotated

from dotenv import load_dotenv, find_dotenv

from pydantic import EmailStr, AnyHttpUrl, BeforeValidator
from pydantic_settings import BaseSettings

load_dotenv(dotenv_path=find_dotenv())


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)

class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv("AUTH_PROJECT_NAME")
    SERVER_NAME: str = os.getenv("AUTH_SERVER_NAME")
    API_V1_STR: str = os.getenv("AUTH_API_V1_STR")

    # Document management config
    DOCS_SERVER_NAME: str = os.getenv("DOCS_SERVER_NAME")

    BACKEND_CORS_ORIGINS : Annotated[
        list[AnyHttpUrl] | str, BeforeValidator(parse_cors)
    ] = list(os.getenv("BACKEND_CORS_ORIGINS"))

    # JWT config
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    TOTP_SECRET_KEY: str = os.getenv("TOTP_SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_SECONDS: int = os.getenv("ACCESS_TOKEN_EXPIRE_SECONDS")
    REFRESH_TOKEN_EXPIRE_SECONDS: int = os.getenv("REFRESH_TOKEN_EXPIRE_SECONDS")
    JWT_ALGO: str = os.getenv("JWT_ALGORITHM")

    MULTI_MAX: int = 20

    # Mongo config
    MONGO_DATABASE_URI: str = os.getenv("MONGO_DATABASE_URI")
    MONGO_DATABASE: str = os.getenv("MONGO_DATABASE")
    if os.getenv("MONGO_REPLICA_SET"):
        MONGO_DATABASE = MONGO_DATABASE+f'&replicaSet={os.getenv("MONGO_REPLICA_SET_NAME")}'

    FIRST_SUPERUSER: EmailStr = os.getenv("FIRST_SUPERUSER")
    FIRST_SUPERUSER_PASSWORD: str = os.getenv("FIRST_SUPERUSER_PASSWORD")


settings = Settings()
