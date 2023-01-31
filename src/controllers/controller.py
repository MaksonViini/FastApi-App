from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from ..database import get_db
from ..models.model import RecordModel
from ..schemas import schema

router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)


class Basic:

    @router.get("/")
    async def main():
        return RedirectResponse(url="/docs/")

    @router.get("/healthchecker")
    async def hello_world():
        return {"Ping": "Pong"}, 200


class Records:

    @router.get("/records")
    async def show_records(db: Session = Depends(get_db)):
        return db.query(RecordModel).all()

    @router.post("/records")
    async def create_record(details: schema.RecordEntity, db: Session = Depends(get_db)):

        to_create = RecordModel(
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
    async def update(id: int, details: schema.RecordEntity, db: Session = Depends(get_db)):
        to_update = {
            RecordModel.date: details.date,
            RecordModel.country: details.country,
            RecordModel.cases: details.cases,
            RecordModel.deaths: details.deaths,
            RecordModel.recoveries: details.recoveries
        }
        db.query(RecordModel).filter(RecordModel.id == id).update(
            to_update, synchronize_session=False)

        db.commit()

        return {'sucess': True}
