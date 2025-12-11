from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.work_order import WorkOrder
from app.schemas.work_order import WorkOrderCreate, WorkOrderRead, WorkOrderUpdate
from app.routers.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/work-orders", tags=["work_orders"])


@router.post("/", response_model=WorkOrderRead, status_code=status.HTTP_201_CREATED)
def create_work_order(
    payload: WorkOrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    wo = WorkOrder(**payload.dict())
    db.add(wo)
    db.commit()
    db.refresh(wo)
    return wo


@router.get("/", response_model=List[WorkOrderRead])
def list_work_orders(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 50,
):
    wos = db.query(WorkOrder).offset(skip).limit(limit).all()
    return wos


@router.get("/{wo_id}", response_model=WorkOrderRead)
def get_work_order(wo_id: int, db: Session = Depends(get_db)):
    wo = db.get(WorkOrder, wo_id)
    if not wo:
        raise HTTPException(status_code=404, detail="Work order not found")
    return wo


@router.put("/{wo_id}", response_model=WorkOrderRead)
def update_work_order(
    wo_id: int,
    payload: WorkOrderUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    wo = db.get(WorkOrder, wo_id)
    if not wo:
        raise HTTPException(status_code=404, detail="Work order not found")

    for field, value in payload.dict(exclude_unset=True).items():
        setattr(wo, field, value)

    db.commit()
    db.refresh(wo)
    return wo
