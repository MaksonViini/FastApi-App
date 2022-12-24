from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

load_dotenv()


SQLALCHEMY_DATABASE_URL = f"""postgresql://postgres:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:
                                                        {os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"""


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
