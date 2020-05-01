from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from b_riders.db.base_class import Base


class Classification(Base):
    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text)
    rides = relationship("Ride")