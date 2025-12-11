from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AppointmentBase(BaseModel):
    branch_id: int
    customer_id: int
    vehicle_id: int
    appointment_datetime: datetime
    status: str = "REQUESTED"
    service_type: Optional[str] = None
    notes: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(AppointmentBase):
    pass

class AppointmentRead(AppointmentBase):
    id: int
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
