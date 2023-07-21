from pydantic import BaseModel
from typing import Optional

class Category(BaseModel):
  id: Optional[str]
  name: str
  amount_words: int
  id_field: str
  status: bool