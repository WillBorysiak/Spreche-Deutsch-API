from pydantic import BaseModel


class CategoriesBase(BaseModel):
    index: int
    name: str
    type: str
    route: str


class CategoriesResponse(CategoriesBase):
    pass

    class Config:
        orm_mode = True
