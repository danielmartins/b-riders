from typing import List, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from b_riders import schemas, models, crud
from b_riders.api_v1 import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.RideInDBBase])
def rides(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve rides.
    """
    rides = crud.ride.get_multi_by_owner(
        db, skip=skip, limit=limit, owner_id=current_user.id
    )
    return rides


@router.post("/", response_model=schemas.RideInDBBase)
def create_ride(
    *,
    db: Session = Depends(deps.get_db),
    ride_in: schemas.RideCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    item = crud.ride.create_with_owner(db=db, obj_in=ride_in, owner_id=current_user.id)
    return item
