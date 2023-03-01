from passlib.context import CryptContext


pass_Context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify(hashed_password, plain_password):
    return pass_Context.verify(plain_password, hashed_password)
