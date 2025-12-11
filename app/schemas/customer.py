from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class CustomerBase(BaseModel):
    full_name: str
    phone: str
    email: Optional[EmailStr] = None
    line_id: Optional[str] = None
    preferred_contact_channel: Optional[str] = None
    preferred_branch_id: Optional[int] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class CustomerRead(CustomerBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
