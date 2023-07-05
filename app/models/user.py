from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
  _id: Optional[str]
  name: str
  lastname:  str
  full_name: str | None = None
  email: str
  identification: str
  profession: str | None = None
  position: str | None = None
  occupation: str
  role: list = []
  status: bool | None = True
  
class UserRegister(User):
  hashed_password: str = None
  
class Login(BaseModel):
  email: str
  password: str