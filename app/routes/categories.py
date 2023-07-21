from fastapi import APIRouter, HTTPException, status
from app.config.db import dbCategories
from app.schema.categories_schema import category_schema, categories_schema
from app.models.category import Category
from bson import ObjectId


categories = APIRouter(
  prefix="/api/categories",
  tags=["Categories"]
)

@categories.get('/')
async def get_all_categories():
  categories = dbCategories.find({{"status": True}})
  if not categories:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="categories not found")
  return categories_schema(categories)

@categories.post('/')
async def create_new_category(category: Category):
  if not category:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="category not created")
  category_id = dbCategories.insert_one(dict(category)).inserted_id
  return {
    "message": "category add successfully",
    "_id": str(category_id)
  }
  
@categories.get('/{id}')
async def get_single_category(id: str):
  category = dbCategories.find_one({"_id": ObjectId(id)})
  if not category:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="category not found")
  return {
    "message": "category found successfully",
    "word": category_schema(category)
  }
  
@categories.delete('/{id}')
async def delete_single_word(id: str):
  category = dbCategories.find_one({"_id": ObjectId(id)})
  if not category:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="category not found")
  dbCategories.delete_one({"_id": ObjectId(id)})
  return {
    "message": "category remove successfully",
    "id_word": id
  }
  
@categories.put('/{id}/inactive-category')
async def update_status_single_category(id: str):
  category_found = dbCategories.find_one({"_id": ObjectId(id)})
  if not category_found:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="category not found")
  updated_category = dbCategories.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"status": False}})
  if not updated_category:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="category not update")
  return {
    "message": "category status updated correctly",
    "id_word": id
  }
