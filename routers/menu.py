from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from settings.database import get_db_connect
from repository import menu
from typing import List
from settings import schemas, models
from settings.oauth2 import get_current_user


router = APIRouter(
    prefix="/menus",
    tags=["Menus"]
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowMenu)
def create_menu(request: schemas.Menu, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return menu.create(request, db)


@router.get('/', response_model=List[schemas.ShowMenu])
def get_menu(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return menu.get_all(db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowMenu)
def get_one_menu(id: int, response: Response, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return menu.show_menu(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_menu(id: int, request: schemas.Menu, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return menu.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_menu(id: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return menu.delete(id, db)
