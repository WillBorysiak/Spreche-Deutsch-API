from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.database.database import database
from app.models.CategoriesModel import Categories
from app.schemas.CategoriesSchema import CategoriesResponse

router = APIRouter()


# get categories
@router.get("/categories", response_model=list[CategoriesResponse])
def get_categories(db: Session = Depends(database)):
    categories = db.query(Categories).all()

    if not categories:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categories cannot be found",
        )

    return categories


# get categories by type
@router.get("/categories/{type}", response_model=list[CategoriesResponse])
def get_word(type: str, db: Session = Depends(database)):
    categories = db.query(Categories).filter(Categories.type == type).all()

    if not categories:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categories with type '{type}' cannot be found.",
        )

    return categories
