import motor.motor_asyncio
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Settings

settings = Settings(config={'env': 'dev'}).config


SQLALCHEMY_DATABASE_URL = f"""postgresql://postgres:{settings.db_password}@{settings.db_host}:
                                                        {settings.db_port}/{settings.db_database}"""

DATABASE_URL = f"""mongodb://root:{settings.db_password}@{settings.db_host}:27017/"""

client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)

database = client['data']
collection = database['data_health']

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
