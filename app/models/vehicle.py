from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    vin = Column(String(64), unique=True, index=True, nullable=True)
    plate_no = Column(String(20), index=True, nullable=False)
    brand = Column(String(100), nullable=True)
    model = Column(String(100), nullable=True)
    model_year = Column(Integer, nullable=True)
    ev_type = Column(String(20), nullable=True)  # BEV / PHEV / HEV
    battery_capacity_kwh = Column(Integer, nullable=True)

    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    customer = relationship("Customer", back_populates="vehicles")
    appointments = relationship("Appointment", back_populates="vehicle")
    work_orders = relationship("WorkOrder", back_populates="vehicle")
