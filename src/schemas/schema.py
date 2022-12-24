from pydantic import BaseModel


class Record(BaseModel):
    id: int
    country: str
    cases: int
    deaths: int
    recoveries: int

    class Config:
        orm_mode = True