# database.py에서 연결한 db를 테이블과 매핑시키는 역할

from sqlalchemy import Column, TEXT, INT, BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Test(Base):
    __tablename__ = "test"

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    name = Column(TEXT, nullable=False)
    number = Column(INT, nullable=False)

# from sqlalchemy import Column, TEXT, INT, BIGINT
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class Test(Base):
#     __tablename__ = "test"

#     id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
#     name = Column(TEXT, nullable=False)
#     number = Column(INT, nullable=False)