from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from repository import orders
from settings.database import get_db_connect
from settings.oauth2 import get_current_user
from settings import schemas, models
from typing import List


router = APIRouter(
    prefix="/orders",
    tags=['Orders']
)


@router.post('/', response_model=schemas.ShowOrder)
def create_order(request: schemas.ShowOrder, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return orders.create(request, db)


@router.get('/{id}', response_model=schemas.ShowOrder)
def get_order(idOrdered: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return orders.show_order(idOrdered, db)


@router.get('/', response_model=List[schemas.ShowOrder])
def get_orders(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return orders.get_all(db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_order(idOrder: int, request: schemas.UpdateOrder, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return orders.update(idOrder, request, db)


@router.get('/nodeliver/')
def orders_not_delivered(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return orders.orders_not_delivered(db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_order(idOrdered: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return orders.delete(idOrdered, db)
