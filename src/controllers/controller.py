from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session

from ..schemas import schema
from ..models.model import Record

from ..database import get_db


router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)


class Basic:

    @router.get("/")
    async def main():
        return RedirectResponse(url="/docs/")

    @router.get("/hello")
    async def hello_world():
        return {"hello": "ok"}, 200


class Records:

    @router.get("/records")
    async def show_records(db: Session = Depends(get_db)):
        return db.query(Record).all()

    @router.post("/records")
    async def create_record(details: schema.Record, db: Session = Depends(get_db)):

        to_create = Record(
            id=details.id,
            date="1/17/2017",
            country=details.country,
            cases=details.cases,
            deaths=details.deaths,
            recoveries=details.recoveries,
        )

        db.add(to_create)
        db.commit()

        return {
            'sucess': True,
            'created_id': to_create.id
        }

    @router.put('/records/{id}')
    async def update(id: int, details: schema.Record, db: Session = Depends(get_db)):
        to_update = {
            Record.date: details.date,
            Record.country: details.country,
            Record.cases: details.cases,
            Record.deaths: details.deaths,
            Record.recoveries: details.recoveries
        }
        db.query(Record).filter(Record.id == id).update(
            to_update, synchronize_session=False)

        db.commit()

        return {'sucess': True}
