from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from settings.database import get_db_connect
from repository import roles
from typing import List
from settings import schemas, models
from settings.oauth2 import get_current_user


router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowRole)
def create_role(request: schemas.Role, db: Session = Depends(get_db_connect)):
    return roles.create(request, db)


@router.get('/', response_model=List[schemas.ShowRole])
def get_roles(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return roles.get_all(db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowRole)
def get_one_role(id: int, response: Response, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return roles.show_role(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_role(id: int, request: schemas.Role, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return roles.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_role(id: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return roles.delete(id, db)
