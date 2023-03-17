from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


class Delivery(BaseModel):
    delivery_quantity: int
    delivery_locations: str
    amount_collected: float
    delivery_date: Optional[datetime] = None
#    commercial_id: int
    user_id: int
    ordered_id: int


class UpdateDeliver(BaseModel):
    delivery_quantity: int
    amount_collected: float


class ShowDeliver(BaseModel):
    idDelivery: int
    delivery_quantity: int
    delivery_locations: str
    amount_collected: float
    delivery_date: Optional[datetime] = None
#    commercial_id: int
    user_id: int
    ordered_id: int

    class Config:
        orm_mode = True


# class Commercial(BaseModel):
#    firstnameOfAgent: str
#    lastnameOfAgent: str
#    addressOfAgent: str
#    agentPhone: str
#    agentState: bool


# class ShowAgent(BaseModel):
#    firstnameOfAgent: str
#    lastnameOfAgent: str
#    addressOfAgent: str
#    agentPhone: str
#    agentState: bool
#    delivers: list[ShowDeliver] = []

#    class Config:
#        orm_mode = True


# class AccountUser(BaseModel):
#    mailOfaccount: str
#    accountState: bool


#class ShowAccount(BaseModel):
#    accountState: bool

#    class Config:
#        orm_mode = True


class User(BaseModel):
    login: str
    passOfUser: str
    email: EmailStr
    firstname: str
    lastname: str
    telephone: str
    role_id: int
    is_active: bool

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    passOfUser: str


class UpdateUserAccount(BaseModel):
    login: str
    email: EmailStr
    firstname: str
    lastname: str
    telephone: str
    is_active: bool


class Ordered(BaseModel):
    ordered_quantity: int
    # ordered_date: datetime
    customer_id: int
    product_id: int


class UpdateOrder(BaseModel):
    ordered_quantity: int
    product_id: int


class ShowOrder(BaseModel):
    idOrdered: int
    ordered_quantity: int
    ordered_date: datetime
    customer_id: int
    product_id: int

    class Config:
        orm_mode = True


class Customer(BaseModel):
    firstnameOfCustomer: str
    lastnameOfCustomer: str
    customerPhone: str
    longitude: float
    latitude: float
    user_id: int


class ShowCustomer(BaseModel):
    idCustomer: int
    firstnameOfCustomer: str
    lastnameOfCustomer: str
    customerPhone: str
    longitude: float
    latitude: float
    orders: list[ShowOrder] = []

    class Config:
        orm_mode = True


class ShowUser(UpdateUserAccount):
    idUser: int
    role_id: int
    delivers: list[ShowDeliver] = []
    customers: list[ShowCustomer] = []

    class Config:
        orm_mode = True


class Menu(BaseModel):
    label: str
    role_id: int


class ShowMenu(BaseModel):
    label: str

    class Config:
        orm_mode = True


class Role(BaseModel):
    label: str


class ShowRole(BaseModel):
    id: int
    label: str
    menus: list[ShowMenu] = []
    users: list[ShowUser] = []

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    login: Optional[str] = None


class Product(BaseModel):
    labelOfProduct: str
    unitPrice: float
    productQuantity: int
    category_id: int


class ShowProduct(BaseModel):
    idProduct: int
    labelOfProduct: str
    unitPrice: float
    productQuantity: int
    category_id: int

    class Config:
        orm_mode = True


class Category(BaseModel):
    id: int
    labelOfCat: str

class ShowCategory(Category):
    products:list[ShowProduct] = []

    class Config:
        orm_mode = True
