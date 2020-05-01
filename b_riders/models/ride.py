from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from b_riders.db.base_class import Base


class Ride(Base):
    id = Column(Integer, primary_key=True, index=True)
    begin = Column(DateTime, nullable=False)
    end = Column(DateTime, nullable=False)
    experience = Column(Integer, nullable=False, default=0)
    classification_id = Column(Integer, ForeignKey("classification.id"))
    classification = relationship("Classification", back_populates="rides")
