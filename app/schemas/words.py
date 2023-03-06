from pydantic import BaseModel


class WordBase(BaseModel):
    index: int
    german: str
    english: str
    gender: str
    category_index: int


class WordResponse(WordBase):
    pass

    class Config:
        orm_mode = True
