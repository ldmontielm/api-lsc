from fastapi import APIRouter, HTTPException, status
from app.config.db import dbPlaces
from app.schema.places_schema import places_schema, place_schema
from app.models.place import Place
from bson import ObjectId


places = APIRouter(
  prefix="/places",
  tags=["Places"]
)

@places.get('/')
async def get_all_places():
  places = dbPlaces.find({})
  if not places:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="places not found")
  return places_schema(places)

@places.post('/')
async def create_new_place(place: Place):
  if not place:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="place not created")
  category_id = dbPlaces.insert_one(dict(place)).inserted_id
  return {
    "message": "place add successfully",
    "_id": str(category_id)
  }
  
@places.get('/{id}')
async def get_single_place(id: str):
  place = dbPlaces.find_one({"_id": ObjectId(id)})
  if not place:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="place not found")
  return {
    "message": "place found successfully",
    "word": place_schema(place)
  }
  
@places.delete('/{id}')
async def delete_single_place(id: str):
  place = dbPlaces.find_one({"_id": ObjectId(id)})
  if not place:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="place not found")
  dbPlaces.delete_one({"_id": ObjectId(id)})
  return {
    "message": "place remove successfully",
    "id_word": id
  }
  
@places.put('/{id}/inactive-place')
async def update_status_single_place(id: str):
  place_found = dbPlaces.find_one({"_id": ObjectId(id)})
  if not place_found:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="place not found")
  updated_place = dbPlaces.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"status": False}})
  if not updated_place:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="place not update")
  return {
    "message": "place status updated correctly",
    "id_word": id
  }