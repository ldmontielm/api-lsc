from fastapi import APIRouter, Depends, HTTPException, status
from app.schema.words_schema import words_schema, word_schema
from app.models.word import Word
from app.config.db import dbWords
from bson import ObjectId

words = APIRouter(
  prefix='/api/words',
  tags=['Words'],
)

@words.get('/')
async def get_all_words():
  words = dbWords.find()
  if not words:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Words not found")
  return words_schema(words)
  
@words.post('/')
async def create_new_word(word: Word):
  if not word:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="word not created")
  word_id = dbWords.insert_one(dict(word)).inserted_id
  return {
    "message": "word add successfully",
    "_id": str(word_id)
  }

@words.get('/{id}')
async def get_single_word(id: str):
  word = dbWords.find_one({"_id": ObjectId(id)})
  if not word:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Word not found")
  return {
    "message": "word found successfully",
    "word": word_schema(word)
  }
  
@words.delete('/{id}')
async def delete_single_word(id: str):
  word = dbWords.find_one({"_id": ObjectId(id)})
  if not word:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Word not found")
  dbWords.delete_one({"_id": ObjectId(id)})
  return {
    "message": "word remove successfully",
    "id_word": id
  }
  
@words.put('/{id}/inactive-word')
async def update_status_single_word(id: str):
  word_found = dbWords.find_one({"_id": ObjectId(id)})
  if not word_found:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Word not found")
  updated_word = dbWords.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"status": False}})
  if not updated_word:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Word not update")
  return {
    "message": "word status updated correctly",
    "id_word": id
  }