from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session

from .config import middleware
from .config import settings
from .database import database
from .models.CategoriesModel import Categories
from .models.SentencesModel import Sentences
from .models.WordsModel import Words
from .schemas.CategoriesSchema import CategoriesResponse
from .schemas.SentencesSchema import SentencesResponse
from .schemas.WordsSchema import WordsResponse

app = FastAPI(middleware=middleware)


# root
@app.get("/")
def root():
    return {"Welcome to the Spreche Deutsch API"}


@app.get("/test")
def root():
    return {"This is a test endpoint", settings.environment}


# CATEGORIES


# get categories
@app.get("/categories", response_model=list[CategoriesResponse])
def get_categories(db: Session = Depends(database)):
    categories = db.query(Categories).all()

    if not categories:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categories cannot be found",
        )

    return categories


# get categories by type
@app.get("/categories/{type}", response_model=list[CategoriesResponse])
def get_word(type: str, db: Session = Depends(database)):
    categories = db.query(Categories).filter(Categories.type == type).all()

    if not categories:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categories with type '{type}' cannot be found.",
        )

    return categories


# WORDS


# get words
@app.get("/words", response_model=list[WordsResponse])
def get_words(db: Session = Depends(database)):
    words = db.query(Words).all()

    if not words:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Words cannot be found",
        )

    return words


# get word by id
@app.get("/words/{id}", response_model=WordsResponse)
def get_word(id: int, db: Session = Depends(database)):
    word = db.query(Words).filter(Words.index == id).first()

    if not word:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Word with id '{id}' cannot be found.",
        )

    return word


# get words by category
@app.get("/words/category/{category}", response_model=list[WordsResponse])
def get_word(category: str, db: Session = Depends(database)):
    words = db.query(Words).filter(Words.category == category).all()

    if not words:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Words with category '{category}' cannot be found.",
        )

    return words


# SENTENCES


# get sentences
@app.get("/sentences", response_model=list[SentencesResponse])
def get_sentences(db: Session = Depends(database)):
    sentences = db.query(Sentences).all()

    if not sentences:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sentences cannot be found",
        )

    return sentences


# get sentence by id
@app.get("/sentences/{id}", response_model=SentencesResponse)
def get_sentence(id: int, db: Session = Depends(database)):
    sentence = db.query(Sentences).filter(Sentences.index == id).first()

    if not sentence:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Sentence with id '{id}' cannot be found.",
        )

    return sentence


# get sentences by category
@app.get("/sentences/category/{category}", response_model=list[SentencesResponse])
def get_word(category: str, db: Session = Depends(database)):
    sentences = db.query(Sentences).filter(Sentences.category == category).all()

    if not sentences:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Sentences with category '{category}' cannot be found.",
        )

    return sentences
