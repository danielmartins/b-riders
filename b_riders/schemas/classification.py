from typing import Optional

from pydantic import BaseModel


class ClassificationBase(BaseModel):
    description: str


class ClassificationCreate(ClassificationBase):
    pass


class ClassificationUpdate(ClassificationBase):
    pass


class ClassificationInDBBase(ClassificationBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True
