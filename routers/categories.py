from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from repository import categories
from settings.database import get_db_connect
from settings.oauth2 import get_current_user
from typing import List
from settings import schemas, models


router = APIRouter(
    prefix="/catgories",
    tags=['Categories']
)


@router.post('/', response_model=schemas.ShowCategory)
def create_category(request: schemas.Category, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return categories.create(request, db)


@router.get('/{id}', response_model=schemas.ShowCategory)
def get_category(id: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return categories.show_category(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_category(id: int, request: schemas.Category, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return categories.update(id, request, db)


@router.get('/', response_model=List[schemas.ShowCategory])
def get_categories(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return categories.get_all(db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_category(id: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return categories.delete(id, db)

