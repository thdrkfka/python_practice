
# 테이블을 만들기 위한 모듈

from sqlalchemy import Column, Integer, Boolean, Text
from database import Base

class Todo(Base):
  # 테이블 이름 설정
  __tablename__ = 'todos'
  # 컬럼 설정
  id = Column(Integer, primary_key=True)
  task = Column(Text)
  completed = Column(Boolean, default=False)