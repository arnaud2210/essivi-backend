from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from repository import delivers
from settings.database import get_db_connect
from settings.oauth2 import get_current_user
from settings import schemas, models
from typing import List


router = APIRouter(
    prefix="/delivers",
    tags=['Delivers']
)


@router.post('/', response_model=schemas.ShowDeliver)
def create_deliver(request: schemas.Delivery, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return delivers.create(request, db)


@router.get('/{id}', response_model=schemas.ShowDeliver)
def get_deliver(idDelivery: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return delivers.show_deliver(idDelivery, db)


@router.get('/', response_model=List[schemas.ShowDeliver])
def get_delivers(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return delivers.get_all(db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_deliver(idDelivery: int, request: schemas.UpdateDeliver, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return delivers.update(idDelivery, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_deliver(idDelivery: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return delivers.delete(idDelivery, db)
