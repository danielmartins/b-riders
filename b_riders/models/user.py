from sqlalchemy import Column, Integer, Boolean, String

from b_riders.db.base_class import Base


class User(Base):
    id = Column("id", Integer, primary_key=True, index=True)
    full_name = Column("full_name", String, index=True)
    email = Column("email", String, unique=True, index=True, nullable=False)
    hashed_password = Column("hashed_password", String(200), nullable=False)
    is_active = Column("is_active", Boolean, default=True)
    is_superuser = Column("is_superuser", Boolean, default=False)