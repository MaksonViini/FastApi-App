from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse
from typing import List
from sqlalchemy.orm import Session

from ..schemas import schema
from ..models import model

from ..database import get_db

router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def main():
    return RedirectResponse(url="/docs/")

@router.get("/hello")
async def hello_world():
    return {"hello": "ok"}, 200


@router.get("/records/", response_model=List[schema.Record])
def show_records(db: Session = Depends(get_db)):
    return db.query(model.Record).all()