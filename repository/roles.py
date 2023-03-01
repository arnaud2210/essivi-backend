from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from settings import schemas, models


def get_all(db: Session):
    roles = db.query(models.Role).all()
    return roles


def create(request: schemas.Role, db: Session):
    new_role = models.Role(label=request.label)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role


def show_role(id: int, db: Session):
    role = db.query(models.Role).filter(models.Role.id == id).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"role with the id {id} doesn't exist")
    return role


def update(id: int, request: schemas.Role, db: Session):
    role = db.query(models.Role).filter(models.Role.id == id).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"role with the id {id} doesn't exist")
    
    role.label = request.label
    db.commit()
    return "updated"


def delete(id: int, db: Session):
    db.query(models.Role).filter(models.Role.id ==
                                 id).delete(synchronize_session=False)
    db.commit()
    return "done"
