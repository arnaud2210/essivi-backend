from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from repository import reports
from settings.database import get_db_connect
from settings.oauth2 import get_current_user
from settings import schemas


router = APIRouter(
    prefix="/reports",
    tags=['Reports']
)


@router.get('/caPerMonth/')
def caPerMonth(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return reports.caPerMonth(db)


@router.get('/numCustomPerAgent/')
def numCustomPerAgent(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return reports.numCustomPerAgent(db)


@router.get('/user_type/')
def user_type(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return reports.user_type(db)


@router.get('/quantityPerCat/')
def quantityPerCat(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return reports.quantityPerCat(db)
