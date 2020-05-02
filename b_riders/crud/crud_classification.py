from b_riders.crud.base import CRUDBase
from b_riders.models.classification import Classification
from b_riders.schemas.classification import ClassificationCreate, ClassificationUpdate


class CRUDClassification(CRUDBase[Classification, ClassificationCreate, ClassificationUpdate]):
    pass


classifications = CRUDClassification(Classification)
