from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from b_riders.crud.base import CRUDBase, CreateSchemaType, ModelType
from b_riders.models.ride import Ride
from b_riders.schemas import RideCreate, RideUpdate


class CRUDRide(CRUDBase[Ride, RideCreate, RideUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: RideCreate, owner_id: int
    ) -> Ride:
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Ride]:
        return (
            db.query(self.model)
            .filter(Ride.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


ride = CRUDRide(Ride)
