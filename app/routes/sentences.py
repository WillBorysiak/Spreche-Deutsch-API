from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session

from app.database import database
from app.models.SentencesModel import Sentences
from app.schemas.SentencesSchema import SentencesResponse

router = APIRouter()


# get sentences
@router.get("/sentences", response_model=list[SentencesResponse])
def get_sentences(db: Session = Depends(database)):
    sentences = db.query(Sentences).all()

    if not sentences:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sentences cannot be found",
        )

    return sentences


# get sentence by id
@router.get("/sentences/{id}", response_model=SentencesResponse)
def get_sentence(id: int, db: Session = Depends(database)):
    sentence = db.query(Sentences).filter(Sentences.index == id).first()

    if not sentence:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Sentence with id {id} cannot be found.",
        )

    return sentence


# get sentences by category
@router.get("/sentences/category/{category}", response_model=list[SentencesResponse])
def get_word(category: str, db: Session = Depends(database)):
    sentences = db.query(Sentences).filter(Sentences.category == category).all()

    if not sentences:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Sentences with category '{category}' cannot be found.",
        )

    return sentences
