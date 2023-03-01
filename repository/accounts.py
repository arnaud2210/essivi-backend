"""from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from hashing import pass_Context
from database import get_db_connect
import schemas
import models


def get_all(db: Session):
    accounts = db.query(models.AccountUser).all()
    return accounts


def create(request: schemas.AccountUser, db: Session):
    new_account = models.AccountUser(mailOfAccount=request.mailOfaccount,
                                     accountState=request.accountState)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account


def show_account(idAccount: int, db: Session):
    account = db.query(models.AccountUser).filter(
        models.AccountUser.idAccount == idAccount).first()
    if not account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the account id {idAccount} doesn't exist")
    return account


def delete(idAccount: int, db: Session):
    db.query(models.AccountUser).filter(models.AccountUser.idAccount ==
                                        idAccount).delete(synchronize_session=False)
    db.commit()
    return {'done'}"""
