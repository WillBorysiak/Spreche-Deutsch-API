from pydantic import BaseSettings
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware


# db config
class Settings(BaseSettings):
    db_hostname: str
    db_port: str
    db_username: str
    db_password: str
    db_name: str

    class Config:
        env_file = ".env"


settings = Settings()

# cors config
origins = ["*"]

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET"],
        allow_headers=["*"],
    )
]
