from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base


class WorkOrder(Base):
    __tablename__ = "work_orders"

    id = Column(Integer, primary_key=True, index=True)
    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)

    service_advisor_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    status = Column(String, nullable=False, default="DRAFT")
    promised_delivery_datetime = Column(DateTime(timezone=True), nullable=True)
    actual_delivery_datetime = Column(DateTime(timezone=True), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    vehicle = relationship("Vehicle", back_populates="work_orders")
    customer = relationship("Customer")
    branch = relationship("Branch")
