from fastapi import FastAPI

from app.config.config import middleware
from app.routes import categories, words, sentences

app = FastAPI(middleware=middleware)

app.include_router(categories.router)
app.include_router(words.router)
app.include_router(sentences.router)


# home route
@app.get("/")
def root():
    return {"Welcome to the Spreche Deutsch API"}
