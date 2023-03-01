"""from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from repository import accounts
from hashing import pass_Context
from database import get_db_connect
from oauth2 import get_current_user
from typing import List
import schemas
import models


router = APIRouter(
    prefix="/accounts",
    tags=['Accounts']
)


@router.post('/', response_model=schemas.ShowAccount)
def create_account(request: schemas.AccountUser, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return accounts.create(request, db)


@router.get('/', response_model=List[schemas.ShowAccount])
def get_accounts(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return accounts.get_all(db)


@router.get('/{id}', response_model=schemas.ShowAccount)
def get_account(idAccount: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return accounts.show_account(idAccount, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_account(idAgent: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return accounts.delete(idAgent, db)"""
