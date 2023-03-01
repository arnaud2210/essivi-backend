from sqlalchemy.orm import Session
from sqlalchemy import select, text
from fastapi import HTTPException, status
from settings import schemas, models
from package.tools import log_message


def get_all(db: Session):
    try:
        categories = db.query(models.Category).all()
        return categories
    except:
        return {log_message}


def create(request: schemas.Category, db: Session):
    try:
        new_category = models.Category(labelOfCat = request.labelOfCat)
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category
    except:
        return {log_message}


def show_category(id: int, db: Session):
    category = db.query(models.Category).filter(
        models.Category.id == id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Category with the id {id} doesn't exist")
    return category


def update(id: int, request: schemas.Category, db: Session):
    try:
        category = db.query(models.Category).filter(
            models.Category.id == id).first()
        
        if not category:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"Category with the id {id} not found")
        
        category.labelOfCat = request.labelOfCat
        db.commit()

        return "updated"
    except:
        return {log_message}


def delete(id: int, db: Session):
    db.query(models.Category).filter(models.Category.id ==
                                 id).delete(synchronize_session=False)
    db.commit()
    return {'done'}
