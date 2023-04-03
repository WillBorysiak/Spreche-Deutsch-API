from sqlalchemy import Column, Integer, String

from ..database import Base


class Words(Base):
    __tablename__ = "words"

    index = Column(Integer, name="index", primary_key=True, nullable=False)
    german = Column(String, name="german", nullable=False)
    english = Column(String, name="english", nullable=False)
    gender = Column(String, name="gender", nullable=False)
    category = Column(String, name="category", nullable=False)
