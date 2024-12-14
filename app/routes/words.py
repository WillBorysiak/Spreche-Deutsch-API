from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session

from app.database.database import database
from app.models.WordsModel import Words
from app.schemas.WordsSchema import WordsResponse

router = APIRouter()


# get words
@router.get("/words", response_model=list[WordsResponse])
def get_words(db: Session = Depends(database)):
    words = db.query(Words).all()

    if not words:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Words cannot be found",
        )

    return words


# get word by id
@router.get("/words/{id}", response_model=WordsResponse)
def get_word(id: int, db: Session = Depends(database)):
    word = db.query(Words).filter(Words.index == id).first()

    if not word:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Word with id {id} cannot be found.",
        )

    return word


# get words by category
@router.get("/words/category/{category}", response_model=list[WordsResponse])
def get_word(category: str, db: Session = Depends(database)):
    words = db.query(Words).filter(Words.category == category).all()

    if not words:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Words with category '{category}' cannot be found.",
        )

    return words
