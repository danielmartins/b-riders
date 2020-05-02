from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from b_riders.db.base_class import Base


class Ride(Base):
    id = Column(Integer, primary_key=True, index=True)
    begin = Column(DateTime(timezone=True), nullable=False)
    end = Column(DateTime(timezone=True), nullable=False)
    experience = Column(Integer, nullable=False, default=0)
    classification_id = Column(Integer, ForeignKey("classification.id"))
    classification = relationship("Classification")
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User")
