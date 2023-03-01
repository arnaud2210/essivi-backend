from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from settings.hashing import verify
from settings.jwt import create_access_token, SECRET_KEY, ALGORITHM
from settings import schemas, database, models


router = APIRouter(
    tags=["Authentication"]
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db_connect)):
    user = db.query(models.User).filter(
        models.User.login == request.username).first()

    role = db.query(models.Role).filter(models.Role.id == user.role_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not verify(user.passOfUser, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = create_access_token(data={"sub": user.login})
    return {"access_token": access_token, "token_type": "bearer", "user_id": user.idUser, "user_login": user.login, "role_id": user.role_id, "label": role.label}
