from pydantic import BaseSettings, AnyHttpUrl
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware


class Settings(BaseSettings):
    environment: str
    db_hostname: str
    db_port: str
    db_username: str
    db_password: str
    db_name: str
    cors_origin: AnyHttpUrl

    class Config:
        env_file = ".env"


settings = Settings()

# cors config
origins = [f"{settings.cors_origin}"]

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET"],
        allow_headers=["*"],
    )
]
