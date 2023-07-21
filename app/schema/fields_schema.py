def field_schema(field) -> dict:
  return {
    "id": str(field["_id"]),
    "name": field["name"],
    "amount_category": field["amount_category"],
    "status": field["status"]
  }
  
  
def fields_schema(fields) -> list:
  return [field_schema(field) for field in fields]