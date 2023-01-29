from database import Base, engine
from models.model import Base

print('Criando database')


def create_db():
    Base.metadata.create_all(bind=engine)


def drop_all():
    Base.metadata.drop_all(bind=engine)


if __name__ == '__main__':
    create_db()
