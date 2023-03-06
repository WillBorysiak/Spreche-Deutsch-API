from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session

from .config import middleware
from .database import database
from .models.words import Words
from .schemas.words import WordResponse

app = FastAPI(middleware=middleware)


# root
@app.get("/")
def root():
    return {"Welcome to the Spreche Deutsch API"}


# get words
@app.get("/words", response_model=list[WordResponse])
def get_words(db: Session = Depends(database)):
    words = db.query(Words).all()
    return words


# get one word
@app.get("/word/{id}", response_model=WordResponse)
def get_word(id: int, db: Session = Depends(database)):
    word = db.query(Words).filter(Words.index == id).first()

    if not word:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Word with id {id} cannot be found",
        )

    return word


# get words by category
@app.get("/words/category/{id}", response_model=list[WordResponse])
def get_word(id: int, db: Session = Depends(database)):
    words = db.query(Words).filter(Words.category_index == id).all()

    if not words:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Words with category {id} cannot be found",
        )

    return words
