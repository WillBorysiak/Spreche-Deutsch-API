from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.database.config import settings

DATABASE_URL = (
    f"postgresql+psycopg://{settings.db_username}:{settings.db_password}@"
    f"{settings.db_hostname}:{settings.db_port}/{settings.db_name}"
)

engine = create_engine(DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def database():
    db = session()
    try:
        yield db
    finally:
        db.close()
