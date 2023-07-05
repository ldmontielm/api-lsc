def wordSchema(word) -> dict:
  return {
    'id': str(word['_id']),
    'word': word['word'],
    'type': word['type'],
    'desc_type': word['desc_type'],
    'example': word['example'],
    'example_exp': word['example_exp'],
    'description': word['description'],
    'category': word['category'],
    'places': word['places'],
    'field': word['field'],
  }

def wordsSchema(words) -> list:
  return [wordSchema(word) for word in words]