from pathlib import Path

from config.db import dbUsers
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, status
from passlib.context import CryptContext
from models.user import Login

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


auth = APIRouter(
  prefix="/auth",
  tags=["Authentication"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password (plain_password, hashed_password):
  return pwd_context.verify(plain_password, hashed_password) 

def get_password_hash(password):
  return pwd_context.hash(password)

def get_user(email: str):
  user = dbUsers.find_one({"email": email})
  if(user):
    newUser = {
      "id": str(user["_id"]),
      "name": user["name"],
      "lastname": user["lastname"],
      "full_name": user["full_name"],
      "email": user["email"],
      "profession": user["profession"],
      "position": user["position"],
      "occupation": user["occupation"],
      "role": user["role"],
      "status": user["status"],
      "hashed_password": user["hashed_password"]
    }
    return newUser
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

def authenticate_user(email: str, password: str):
  user = dict(get_user(email))
 
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
  if not verify_password(password, user["hashed_password"]):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="password not match")
    
  newUser = {
    "id": user["id"],
    "name": user["name"],
    "lastname": user["lastname"],
    "full_name": user["full_name"],
    "email": user["email"],
    "profession": user["profession"],
    "position": user["position"],
    "occupation": user["occupation"],
    "role": user["role"],
    "status": user["status"],
  }
  return newUser;


@auth.post('/login')
async def login(login: Login):
  user = authenticate_user(login.email, login.password)
  return user