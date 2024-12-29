from pydantic import BaseModel, ConfigDict


class SentencesBase(BaseModel):
    index: int
    german: str
    english: str
    category: str


class SentencesResponse(SentencesBase):
    model_config = ConfigDict(from_attributes=True)
