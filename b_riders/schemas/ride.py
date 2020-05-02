from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RideBase(BaseModel):
    begin: datetime
    end: datetime
    experience: int
    classification_id: int


class RideCreate(RideBase):
    pass


class RideUpdate(RideBase):
    pass


class RideInDBBase(RideBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True
