from sqlalchemy import Column, Integer, String

from ..database import Base


class Sentences(Base):
    __tablename__ = "sentences"

    index = Column(Integer, name="index", primary_key=True, nullable=False)
    german = Column(String, name="german", nullable=False)
    english = Column(String, name="english", nullable=False)
    category_index = Column(Integer, name="category_index", nullable=False)
