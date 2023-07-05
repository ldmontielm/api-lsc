from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes.words import words
from routes.auth import auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
  "*"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)

app.include_router(words)
app.include_router(auth)
@app.get('/', )
async def root():
  return {"Word":"Hola mundo"}