from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from settings.hashing import pass_Context
from settings import schemas, models
from package.tools import log_message
from settings.mailgun import send_email
# from starlette.responses import JSONResponse
# from fastapi_mail import FastMail, MessageSchema, MessageType
# from routers.sendmail import html, conf


def get_all(db: Session):
    try:
        users = db.query(models.User).order_by(
            models.User.firstname.asc(), models.User.lastname.asc()).all()
        return users
    except:
        return {log_message}


def create(request: schemas.User, db: Session):
    try:
        hashedPassword = pass_Context.hash(request.passOfUser)
        new_user = models.User(login=request.login, passOfUser=hashedPassword, email=request.email, firstname=request.firstname,
                               lastname=request.lastname, telephone=request.telephone, role_id=request.role_id, is_active=request.is_active)
        print(new_user)

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        print(new_user.email)

        api_key = "eadc42023cde51c34cf308d29e5d8a77-15b35dee-1f073036"
        domain = "sandbox97deeaf6ddac4fc09bbe22b11a716626.mailgun.org"
        from_email = "brad@sandbox97deeaf6ddac4fc09bbe22b11a716626.mailgun.org"
        to_email = new_user.email
        subject = "ESSIVI-SARL your agent account"
        message = f"Your login is : {request.login} and your password is : {request.passOfUser}"

        response = send_email(api_key, domain, from_email,
                              to_email, subject, message)
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


def update_account(idUser: int, request: schemas.UpdateUserAccount, db: Session):
    user = db.query(models.User).filter(
        models.User.idUser == idUser).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {idUser} not found")

    user.login = request.login
    user.email = request.email
    user.firstname = request.firstname
    user.lastname = request.lastname
    user.telephone = request.telephone
    user.is_active = request.is_active
    db.commit()
    return "updated"


def delete(idUser: int, db: Session):
    db.query(models.User).filter(models.User.idUser ==
                                 idUser).delete(synchronize_session=False)
    db.commit()
    return f"Succefull deleted {idUser}"
