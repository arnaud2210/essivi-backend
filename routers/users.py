from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from settings.database import get_db_connect
from repository import users
from settings import schemas, models
from typing import List
from settings.oauth2 import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db_connect)):
    return users.create(request, db)


@router.get('/', response_model=List[schemas.ShowUser])
def get_users(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return users.get_all(db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def get_one_user(idUser: int, response: Response, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return users.show_user(idUser, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_user(idUser: int, request: schemas.UpdateUser, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return users.update(idUser, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(idUser: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return users.delete(idUser, db)
