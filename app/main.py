from fastapi import FastAPI
from app.routes.words import words
from app.routes.auth import auth
from app.routes.fields import fields
from app.routes.categories import categories
from app.routes.places import places
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
app.include_router(fields)
app.include_router(categories)
app.include_router(places)

@app.get('/')
async def root():
  count_words = db.words.count_documents({})
  count_fields = db.fields.count_documents({})
  count_categories = db.categories.count_documents({})
  count_places = db.places.count_documents({})
  return [
      {
        "amount_documents": count_words,
        "name": "palabras",
      },
      {
        "amount_documents": count_fields,
        "name": "campos",
      },
      {
        "amount_documents": count_categories,
        "name": "categorias",
      },
      {
        "amount_documents": count_places,
        "name": "territorios",
      }
    ]
