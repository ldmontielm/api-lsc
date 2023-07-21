from pydantic import BaseModel
from typing import Optional

class Field(BaseModel):
  _id: Optional[str]
  name: str 
  amount_category: int
  status: bool