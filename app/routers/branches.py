from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.branch import Branch
from app.schemas.branch import BranchCreate, BranchRead, BranchUpdate
from app.routers.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/branches", tags=["branches"])


@router.post("/", response_model=BranchRead, status_code=status.HTTP_201_CREATED)
def create_branch(
    payload: BranchCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    branch = Branch(**payload.dict())
    db.add(branch)
    db.commit()
    db.refresh(branch)
    return branch


@router.get("/", response_model=List[BranchRead])
def list_branches(db: Session = Depends(get_db)):
    branches = db.query(Branch).all()
    return branches


@router.get("/{branch_id}", response_model=BranchRead)
def get_branch(branch_id: int, db: Session = Depends(get_db)):
    branch = db.get(Branch, branch_id)
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch


@router.put("/{branch_id}", response_model=BranchRead)
def update_branch(
    branch_id: int,
    payload: BranchUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    branch = db.get(Branch, branch_id)
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    for field, value in payload.dict(exclude_unset=True).items():
        setattr(branch, field, value)

    db.commit()
    db.refresh(branch)
    return branch
