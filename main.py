from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routes.words import words
from app.routes.auth import auth
from fastapi.middleware.cors import CORSMiddleware
from app.config.db import db


app = FastAPI()

origins = [
  "*"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)

app.include_router(words)
app.include_router(auth)

@app.get('/')
async def root():
  count = db.words.count_documents({})
  return {
    "count": count,
    "url": "http://localhost:8000/api/words",
    "methods": ["GET", "POST", "PUT", "DELETE"],
  }