# 데이터베이스에 관련된 모듈 관리

# 데이터베이스 연결 객체 만듬

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 파이썬에서 가장 많이 사용되는 "내장 DB 라이브러리"

DB_URL = 'sqlite:///todo.sqlite3'
# 데이터베이스 파일 경로를 지정한 변수. sqlite 데이터베이스를 사용
# todo.sqlite3 이라는 파일 생성 후 사용

# 데이터베이스 엔진 생성
engine = create_engine(DB_URL)

# 연결 세션을 생성하기 위한 객체 생성
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# 베이스를 상속받으면 우리가 만든 데이터베이스에 테이블로 존재함(Entity 같은 개념..?)
# 모든 모델 클래스가 상속받을 기본 모델 클래스로 지정하는 메소드