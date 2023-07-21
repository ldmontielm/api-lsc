def word_schema(word) -> dict:
  return {
    "id": str(word["_id"]),
    "word": word["word"],
    "type": word["type"],
    "desc_type": word["desc_type"],
    "example": word["example"],
    "example_exp": word["example_exp"],
    "id_category": word["id_category"],
    "description": word["description"],
    "id_place": word["id_place"],
    "status": word["status"]
  }

def words_schema(words) -> list:
  return [word_schema(word) for word in words]