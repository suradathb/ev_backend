from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    phone = Column(String, nullable=False, index=True)
    email = Column(String, nullable=True)
    line_id = Column(String, nullable=True)
    preferred_contact_channel = Column(String, nullable=True)

    preferred_branch_id = Column(Integer, ForeignKey("branches.id"), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    preferred_branch = relationship("Branch", back_populates="customers")
    vehicles = relationship("Vehicle", back_populates="customer")
