from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from pydantic import Field
from pydantic_settings import BaseSettings


# env config

class Settings(BaseSettings):
    environment: str = Field(validation_alias="ENVIRONMENT")
    db_hostname: str = Field(validation_alias="DB_HOSTNAME")
    db_port: str = Field(validation_alias="DB_PORT")
    db_username: str = Field(validation_alias="DB_USERNAME")
    db_password: str = Field(validation_alias="DB_PASSWORD")
    db_name: str = Field(validation_alias="DB_NAME")
    cors_origin: str = Field(validation_alias="CORS_ORIGIN")

    class Config:
        env_file = ".env"


settings = Settings()

# cors config

origins = [settings.cors_origin]

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]
