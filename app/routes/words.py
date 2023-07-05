from fastapi import APIRouter, HTTPException, status, Response
from config.db import db, conn
from schema.word import wordSchema, wordsSchema
from bson.objectid import ObjectId
from utils.filters import create_filters
from models.word import Word

words = APIRouter(
  prefix='/api/words',
  tags=['Words'],
)

@words.get('/')
async def get_all_words(word: str | None = "", type: str | None = "", city: str | None = "", field: str | None = "", category: str | None = ""):
  filters = create_filters(word, type, city, field, category)
  if not filters:
    words = db.words.find({})
  else:
    words = db.words.find(filters)
  if not words:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="words not found")
  result = wordsSchema(words)
  return result
  

@words.get('/{id}')
async def get_single_word(id: str):
  word = db.words.find_one({"_id": ObjectId(id)})
  if not word:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="word not found")
 
  print("Mundo")
  return wordSchema(word)
  
@words.post('/')
async def create_word(word: Word):
  new_word = dict(word)
  if not new_word:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="word not create")
  id = db.words.insert_one(new_word).inserted_id
  return {
    "id": str(id),
    "message": "word add successfully"
  }

@words.put('/{id}')
async def update_word(id: str, word: Word):
  word_update = dict(word)
  del word_update['id']
  db.words.find_one_and_update({'_id': ObjectId(id)}, {'$set': word_update})
  return {
    "message": "word update successfully"
  }

@words.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def word_delete(id: str):
  db.words.find_one_and_delete({'_id': ObjectId(id)})
  return Response(status_code=status.HTTP_204_NO_CONTENT)