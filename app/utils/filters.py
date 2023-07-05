def create_filters(
  word: str | None = "", 
  type: str | None = "", 
  city: str | None = "",
  field: str | None = "",
  category: str | None = "",
  ) -> dict:
  filters = {}
  if word:
    filters['$or'] = [
      {'word': {'$regex': word, '$options': 'i'}}
    ]
  if type:
    filters['type'] = type
  if city:
    filters['places'] = {'$in': [city]}
  if field:
    filters['field'] = field
  if category:
    filters['category'] = category
  return filters