#  1. database.py에 저장되어 있는 db 정보들을 이용해 db 세션을 열어서 연결하고
#  2. 기존 db와 매핑된 models.py를 가져와서
#  3. query를 이용해 filter를 설정해서 db 값을 가져오기

from fastapi import FastAPI, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .database import engine, get_db
from .models import Test

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.on_event("startup")
def on_startup():
    Test.metadata.create_all(bind=engine)

@app.get("/")
async def read_root(request: Request, db: Session = Depends(get_db)):
    items = db.query(Test).all()
    return templates.TemplateResponse("index.html", {"request": request, "items": items})
