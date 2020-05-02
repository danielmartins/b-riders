from typing import List, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from b_riders import schemas, models, crud
from b_riders.api_v1 import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.ClassificationInDBBase])
def read_classifications(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve rides.
    """
    return crud.classifications.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=schemas.ClassificationInDBBase)
def create_classification(
    *,
    db: Session = Depends(deps.get_db),
    classification_in: schemas.ClassificationCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    item = crud.classifications.create(db=db, obj_in=classification_in)
    return item
