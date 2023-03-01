from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()


# SQLALCHEMY_DATABASE_URL = "sqlite:///./water.db"
SQLALCHEMY_DATABASE_URL = "postgresql://nerzfljoxnpkbg:140838ccdbf245b51eab94408a30fb8ca15f74164337fee312c5d15c42f141be@ec2-52-3-2-245.compute-1.amazonaws.com:5432/dau5tnduajtloi"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db_connect():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
