from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WorkOrderBase(BaseModel):
    branch_id: int
    customer_id: int
    vehicle_id: int
    service_advisor_id: Optional[int] = None
    status: str = "DRAFT"
    promised_delivery_datetime: Optional[datetime] = None
    actual_delivery_datetime: Optional[datetime] = None

class WorkOrderCreate(WorkOrderBase):
    pass

class WorkOrderUpdate(WorkOrderBase):
    pass

class WorkOrderRead(WorkOrderBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
