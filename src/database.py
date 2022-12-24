from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import database_config

SQLALCHEMY_DATABASE_URL = f"""postgresql://postgres:{database_config['password']}@{database_config['host']}:
                                                        {database_config['port']}/{database_config['database']}"""

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db 
    finally:
        db.close()