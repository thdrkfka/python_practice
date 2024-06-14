# database.py에서 연결한 db를 테이블과 매핑시키는 역할

from sqlalchemy import *
from .database import Base

class Test(Base):
    __tablename__ = "test"

    id = Column(BIGINT, primary_key=True, index=True, autoincrement=True)
    name = Column(TEXT, nullable=False)
    number = Column(INT, nullable=False)

class IAM(Base):
    __tablename__ = "iam"

    id = Column(BIGINT, primary_key=True, index=True, autoincrement=True)
    image = Column(TEXT)
    time = Column(DateTime)
    