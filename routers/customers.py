from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from repository import customers
from settings.database import get_db_connect
from settings.oauth2 import get_current_user
from typing import List
from settings import schemas, models


router = APIRouter(
    prefix="/customers",
    tags=['Customers']
)


@router.post('/', response_model=schemas.ShowCustomer)
def create_customer(request: schemas.Customer, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return customers.create(request, db)


@router.get('/{id}', response_model=schemas.ShowCustomer)
def get_customer(idCustomer: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return customers.show_customer(idCustomer, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_customer(idCustomer: int, request: schemas.Customer, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return customers.update(idCustomer, request, db)


@router.get('/invoices/')
def get_invoices(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return customers.get_invoices(db)


# @router.get('/invoices/{id}')
# def get_one_invoice(idCustomer: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
#    return customers.get_invoice(idCustomer, db)


@router.get('/', response_model=List[schemas.ShowCustomer])
def get_customers(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return customers.get_all(db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(idCustomer: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return customers.delete(idCustomer, db)
