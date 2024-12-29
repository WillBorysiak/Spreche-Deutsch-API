from pydantic import BaseModel, ConfigDict


class WordsBase(BaseModel):
    index: int
    german: str
    english: str
    gender: str
    category: str


class WordsResponse(WordsBase):
    model_config = ConfigDict(from_attributes=True)
