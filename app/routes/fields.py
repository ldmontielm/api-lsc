from fastapi import APIRouter, HTTPException, status
from app.config.db import dbFields
from app.schema.fields_schema import fields_schema, field_schema
from app.models.field import Field
from bson import ObjectId


fields = APIRouter(
  prefix="/api/fields",
  tags=["Fields"]
)

@fields.get('/')
async def get_all_fields():
  fields = dbFields.find({"status": True})
  if not fields:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="fields not found")
  return fields_schema(fields)

@fields.post('/')
async def create_new_word(field: Field):
  if not field:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="field not created")
  field_id = dbFields.insert_one(dict(field)).inserted_id
  return {
    "message": "field add successfully",
    "_id": str(field_id)
  }

@fields.get('/{id}')
async def get_single_word(id: str):
  field = dbFields.find_one({"_id": ObjectId(id)})
  if not field:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="field not found")
  return {
    "message": "field found successfully",
    "word": field_schema(field)
  }

@fields.delete('/{id}')
async def delete_single_word(id: str):
  field = dbFields.find_one({"_id": ObjectId(id)})
  if not field:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Field not found")
  dbFields.delete_one({"_id": ObjectId(id)})
  return {
    "message": "field remove successfully",
    "id_word": id
  }

@fields.put('/{id}/inactive-field')
async def update_status_single_field(id: str):
  field_found = dbFields.find_one({"_id": ObjectId(id)})
  if not field_found:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Field not found")
  updated_field = dbFields.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"status": False}})
  if not updated_field:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Field not update")
  return {
    "message": "field status updated correctly",
    "id_word": id
  }