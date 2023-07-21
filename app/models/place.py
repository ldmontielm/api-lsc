from pydantic import BaseModel
from typing import Optional

class Place(BaseModel):
  _id: Optional[str]
  name: str
  status: bool