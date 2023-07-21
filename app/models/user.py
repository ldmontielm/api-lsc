from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
  _id: Optional[str]
  name: str
  lastname:  str
  full_name: Optional[str]
  email: str
  identification: str
  profession: str
  position: str 
  occupation: str
  role: list = []
  status: Optional[bool] = True
  
class UserRegister(User):
  hashed_password: str = None
  
class Login(BaseModel):
  email: str
  password: str