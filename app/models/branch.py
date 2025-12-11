from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.core.database import Base


class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    province = Column(String, nullable=True)
    country = Column(String, nullable=True)
    phone = Column(String, nullable=True)

    is_active = Column(Boolean, default=True)

    users = relationship("User", back_populates="branch")
    customers = relationship("Customer", back_populates="preferred_branch")
