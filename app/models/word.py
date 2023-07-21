from pydantic import BaseModel
from typing import Optional

class Word(BaseModel):
  _id: Optional[str]
  word: str
  type: str
  desc_type: str
  example: str
  example_exp: str
  description: str
  id_category: str
  id_place: str
  status: bool = True