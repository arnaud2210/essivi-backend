from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from settings.hashing import pass_Context
from settings import schemas, models
from package.tools import log_message
from settings.config import settings
from settings.utils import send_new_account_email
# from starlette.responses import JSONResponse
# from fastapi_mail import FastMail, MessageSchema, MessageType
# from routers.sendmail import html, conf


def get_all(db: Session):
    try:
        users = db.query(models.User).all()
        return users
    except:
        return {log_message}


def create(request: schemas.User, db: Session):
    try:
        hashedPassword = pass_Context.hash(request.passOfUser)
        new_user = models.User(login=request.login, passOfUser=hashedPassword, email=request.email, firstname=request.firstname,
                               lastname=request.lastname, telephone=request.telephone, role_id=request.role_id, is_active=request.is_active)
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        if settings.EMAILS_ENABLED and new_user.email:
            send_new_account_email(
                email_to=new_user.email, username=new_user.login, password=new_user.passOfUser
            )
        return new_user

    except:
        return {log_message}


def show_user(idUser: int, db: Session):
    user = db.query(models.User).filter(models.User.idUser == idUser).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {idUser} doesn't exist")
    return user


def update(idUser: int, request: schemas.UpdateUser, db: Session):
    user = db.query(models.User).filter(
        models.User.idUser == idUser).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {idUser} not found")

    user.passOfUser = pass_Context.hash(request.passOfUser)
    db.commit()
    return "updated"


def delete(idUser: int, db: Session):
    db.query(models.User).filter(models.User.idUser ==
                                 idUser).delete(synchronize_session=False)
    db.commit()
    return "done"
