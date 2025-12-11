from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)

    appointment_datetime = Column(DateTime(timezone=True), nullable=False)
    status = Column(String, nullable=False, default="REQUESTED")
    service_type = Column(String, nullable=True)
    notes = Column(String, nullable=True)

    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    branch = relationship("Branch")
    customer = relationship("Customer")
    vehicle = relationship("Vehicle", back_populates="appointments")
