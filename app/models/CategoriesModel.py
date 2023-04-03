from sqlalchemy import Column, Integer, String

from ..database import Base


class Categories(Base):
    __tablename__ = "categories"

    index = Column(Integer, name="index", primary_key=True, nullable=False)
    name = Column(String, name="name", nullable=False)
    type = Column(String, name="type", nullable=False)
    route = Column(String, name="route", nullable=False)
