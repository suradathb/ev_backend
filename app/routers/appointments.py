from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate, AppointmentRead, AppointmentUpdate
from app.routers.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/appointments", tags=["appointments"])


@router.post("/", response_model=AppointmentRead, status_code=status.HTTP_201_CREATED)
def create_appointment(
    payload: AppointmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    appointment = Appointment(**payload.dict(), created_by=current_user.id)
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment


@router.get("/", response_model=List[AppointmentRead])
def list_appointments(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 50,
):
    appointments = db.query(Appointment).offset(skip).limit(limit).all()
    return appointments


@router.get("/{appointment_id}", response_model=AppointmentRead)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.get(Appointment, appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment


@router.put("/{appointment_id}", response_model=AppointmentRead)
def update_appointment(
    appointment_id: int,
    payload: AppointmentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    appointment = db.get(Appointment, appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    for field, value in payload.dict(exclude_unset=True).items():
        setattr(appointment, field, value)

    db.commit()
    db.refresh(appointment)
    return appointment
