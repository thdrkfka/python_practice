#  1. database.py에 저장되어 있는 db 정보들을 이용해 db 세션을 열어서 연결하고
#  2. 기존 db와 매핑된 models.py를 가져와서
#  3. query를 이용해 filter를 설정해서 db 값을 가져오기

from fastapi import FastAPI, Depends, Path, HTTPException
from pydantic import BaseModel
from database import engine, get_db
from models import Test
from sqlalchemy.orm import Session
from . import models

app = FastAPI()

@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def first_get(db: Session = Depends(get_db)):
    items = db.query(Test).all()
    return items