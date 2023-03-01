from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from repository import products
from settings.database import get_db_connect
from settings.oauth2 import get_current_user
from typing import List
from settings import schemas, models


router = APIRouter(
    prefix="/products",
    tags=['Products']
)


@router.post('/', response_model=schemas.ShowProduct)
def create_product(request: schemas.Product, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return products.create(request, db)


@router.get('/{id}', response_model=schemas.ShowProduct)
def get_product(idProduct: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return products.show_product(idProduct, db)


@router.get('/details/')
def get_details(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return products.get_details(db)


@router.get('/', response_model=List[schemas.ShowProduct])
def get_products(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return products.get_all(db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_product(idProduct: int, request: schemas.ShowProduct, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return products.update(idProduct, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(idProduct: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return products.delete(idProduct, db)
