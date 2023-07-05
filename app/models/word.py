from pydantic import BaseModel
from typing import Optional

class Video(BaseModel):
  name: str
  url: str

class Word(BaseModel):
  id: Optional[str]
  word: str
  type: str
  desc_type: str
  example: str
  example_exp: str
  description: str
  category: str
  places: list[str]
  field: str