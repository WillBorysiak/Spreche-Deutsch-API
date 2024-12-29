from pydantic import BaseModel, ConfigDict


class CategoriesBase(BaseModel):
    index: int
    name: str
    type: str
    route: str


class CategoriesResponse(CategoriesBase):
    model_config = ConfigDict(from_attributes=True)
