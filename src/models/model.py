from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from typing import List

# Retirar os dois pontos para executar o create_db
from ..database import Base, get_db

db = get_db()


class Record(Base):
    __tablename__ = "Records"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    country = Column(String(255), index=True)
    cases = Column(Integer)
    deaths = Column(Integer)
    recoveries = Column(Integer)

    @classmethod
    def find_by_id(cls, _id: int) -> 'Record':
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List['Record']:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
