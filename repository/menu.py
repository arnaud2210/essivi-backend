from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status
from settings import schemas, models


def get_all(db: Session):
    menus = db.query(models.Menu).all()
    return menus


def create(request: schemas.Menu, db: Session):
    new_menu = models.Menu(label=request.label, role_id=request.role_id)
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu


def show_menu(id: int, db: Session):
    menu = db.query(models.Menu).filter(models.Menu.id == id).first()
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"menu with the id {id} doesn't exist")
    return menu


def update(id: int, request: schemas.Role, db: Session):
    menu = db.query(models.Menu).filter(models.Menu.id == id).first()
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"menu with the id {id} doesn't exist")
    
    menu.label = request.label
    db.commit()
    return "updated"


def delete(id: int, db: Session):
    db.query(models.Menu).filter(models.Menu.id ==
                                 id).delete(synchronize_session=False)
    db.commit()
    return "done"
