from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session

from .config import middleware
from .database import database
from .models.SentencesModel import Sentences
from .models.WordsModel import Words
from .schemas.SentencesSchema import SentencesResponse
from .schemas.WordsSchema import WordsResponse

app = FastAPI(middleware=middleware)


# root
@app.get("/")
def root():
    return {"Welcome to the Spreche Deutsch API"}


# WORDS


# get words
@app.get("/words", response_model=list[WordsResponse])
def get_words(db: Session = Depends(database)):
    words = db.query(Words).all()
    return words


# get one word
@app.get("/words/{id}", response_model=WordsResponse)
def get_word(id: int, db: Session = Depends(database)):
    word = db.query(Words).filter(Words.index == id).first()

    if not word:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Word with id {id} cannot be found",
        )

    return word


# get words by category
@app.get("/words/category/{id}", response_model=list[WordsResponse])
def get_word(id: int, db: Session = Depends(database)):
    words = db.query(Words).filter(Words.category_index == id).all()

    if not words:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Words with category {id} cannot be found",
        )

    return words


# SENTENCES


# get sentences
@app.get("/sentences", response_model=list[SentencesResponse])
def get_sentences(db: Session = Depends(database)):
    sentences = db.query(Sentences).all()
    return sentences


# get one sentence
@app.get("/sentences/{id}", response_model=SentencesResponse)
def get_sentence(id: int, db: Session = Depends(database)):
    sentence = db.query(Sentences).filter(Sentences.index == id).first()

    if not sentence:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Word with id {id} cannot be found",
        )

    return sentence


# get words by sentences
@app.get("/sentences/category/{id}", response_model=list[SentencesResponse])
def get_word(id: int, db: Session = Depends(database)):
    sentences = db.query(Sentences).filter(Sentences.category_index == id).all()

    if not sentences:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Words with category {id} cannot be found",
        )

    return sentences
