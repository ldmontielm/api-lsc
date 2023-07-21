def category_schema(category) -> dict:
  return {
    "id": str(category["_id"]),
    "name": category["name"],
    "amount_words": category["amount_words"],
    "id_field": category["id_field"],
    "status": category["status"]
  }
  
def categories_schema(categories) -> list:
  return [category_schema(category) for category in categories]