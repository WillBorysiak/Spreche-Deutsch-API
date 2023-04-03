from pydantic import BaseModel


class WordsBase(BaseModel):
    index: int
    german: str
    english: str
    gender: str
    category: str


class WordsResponse(WordsBase):
    pass

    class Config:
        orm_mode = True
