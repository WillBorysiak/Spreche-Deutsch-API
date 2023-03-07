from pydantic import BaseModel


class SentencesBase(BaseModel):
    index: int
    german: str
    english: str
    category_index: int


class SentencesResponse(SentencesBase):
    pass

    class Config:
        orm_mode = True
