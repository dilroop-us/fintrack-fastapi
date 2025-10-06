from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app import models
from app.schemas import CategoryCreate, CategoryUpdate, CategoryOut
from app.auth import get_current_user

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/", response_model=List[CategoryOut])
def list_categories(db: Session = Depends(get_db), user=Depends(get_current_user)):
    q = db.query(models.Category).filter(models.Category.user_id == user.id).order_by(models.Category.name.asc())
    return q.all()

@router.post("/", response_model=CategoryOut, status_code=201)
def create_category(payload: CategoryCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    cat = models.Category(user_id=user.id, name=payload.name, type=payload.type)  # type: ignore
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat

@router.put("/{category_id}", response_model=CategoryOut)
def update_category(category_id: int, payload: CategoryUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    cat = db.query(models.Category).filter(models.Category.id == category_id, models.Category.user_id == user.id).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")
    if payload.name is not None:
        cat.name = payload.name
    if payload.type is not None:
        cat.type = payload.type  # type: ignore
    db.commit()
    db.refresh(cat)
    return cat

@router.delete("/{category_id}", status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    cat = db.query(models.Category).filter(models.Category.id == category_id, models.Category.user_id == user.id).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(cat)
    db.commit()
    return
