from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VehicleBase(BaseModel):
    vin: Optional[str] = None
    plate_no: str
    brand: Optional[str] = None
    model: Optional[str] = None
    model_year: Optional[int] = None
    ev_type: Optional[str] = None
    battery_capacity_kwh: Optional[int] = None
    customer_id: int

class VehicleCreate(VehicleBase):
    pass

class VehicleUpdate(VehicleBase):
    pass

class VehicleRead(VehicleBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
