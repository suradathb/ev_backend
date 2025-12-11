from pydantic import BaseModel
from typing import Optional

class BranchBase(BaseModel):
    code: str
    name: str
    address: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    country: Optional[str] = None
    phone: Optional[str] = None
    is_active: bool = True

class BranchCreate(BranchBase):
    pass

class BranchUpdate(BranchBase):
    pass

class BranchRead(BranchBase):
    id: int

    class Config:
        orm_mode = True
