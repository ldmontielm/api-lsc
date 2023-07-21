def place_schema(place) -> dict:
  return {
    "id": str(place["_id"]),
    "name": place["name"],
    "status": place["status"]
  }
  
def places_schema(places) -> list:
  return [place_schema(place) for place in places]