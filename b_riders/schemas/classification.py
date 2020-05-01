from pydantic import BaseModel


class ClassificationCreate(BaseModel):
    description: str


class ClassificationUpdate(BaseModel):
    description: str
