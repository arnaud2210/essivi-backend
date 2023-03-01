from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from settings.database import Base
from datetime import datetime


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String)

    users = relationship("User", back_populates="roles")
    menus = relationship("Menu", back_populates="roles")


class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String)
    role_id = Column(Integer, ForeignKey('roles.id'))

    roles = relationship("Role", back_populates="menus")


class User(Base):
    __tablename__ = 'users'
    
    idUser = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True)
    passOfUser = Column(String)
    email = Column(String, unique=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    telephone = Column(String, unique=True, index=True)
    role_id = Column(Integer, ForeignKey('roles.id'))
    is_active = Column(Boolean)

    roles = relationship("Role", back_populates="users")
    delivers = relationship("Delivery", back_populates="users")
    customers = relationship("Customer", back_populates="users")

#    type = Column(String)
#    __mapper_args__ = {
#        'polymorphic_on': type,
#        'polymorphic_identity': 'users'
#    }


# class AccountUser(User):
#    __tablename__ = 'accounts'
    
#    __mapper_args__ = {'polymorphic_identity': 'accounts'}
#    idAccount = Column(None, ForeignKey('users.idUser'), primary_key=True, index=True)
#    mailOfAccount = Column(String, unique=True, index=True)
#    accountState = Column(Boolean)


# class Commercial(User):
#    __tablename__ = 'commercials'

#    __mapper_args__ = {'polymorphic_identity': 'commercials'}
#    idAgent = Column(None, ForeignKey('users.idUser'), primary_key=True, index=True)
#    firstnameOfAgent = Column(String)
#    lastnameOfAgent = Column(String)
#    addressOfAgent = Column(String)
#    agentPhone = Column(String, unique=True, index=True)
#    agentState = Column(Boolean)

#    delivers = relationship("Delivery", back_populates="commercials")


class Customer(Base):
    __tablename__ = "customers"

    idCustomer = Column(Integer, primary_key=True, index=True)
    firstnameOfCustomer = Column(String)
    lastnameOfCustomer = Column(String)
    customerPhone = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    user_id = Column(Integer, ForeignKey('users.idUser'))

    orders = relationship("Ordered", back_populates="customers")
    users = relationship("User", back_populates="customers")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    labelOfCat = Column(String)

    products = relationship("Product", back_populates="categories")


class Product(Base):
    __tablename__ = "products"

    idProduct = Column(Integer, primary_key=True, index=True)
    labelOfProduct = Column(String)
    unitPrice = Column(Float)
    productQuantity = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))

    orders = relationship("Ordered", back_populates="products")
    categories = relationship("Category", back_populates="products")


class Ordered(Base):
    __tablename__ = "orders"

    idOrdered = Column(Integer, primary_key=True, index=True)
    ordered_quantity = Column(Integer)
    ordered_date = Column(DateTime, default=datetime.now())
    customer_id = Column(Integer, ForeignKey('customers.idCustomer'))
    product_id = Column(Integer, ForeignKey('products.idProduct'))

    customers = relationship("Customer", back_populates="orders")
    products = relationship("Product", back_populates="orders")
    delivers = relationship("Delivery", back_populates="orders")


class Delivery(Base):
    __tablename__ = "delivers"

    idDelivery = Column(Integer, primary_key=True, index=True)
    delivery_quantity = Column(Integer)
    delivery_locations = Column(String)
    amount_collected = Column(Float)
    delivery_date = Column(DateTime, default=datetime.now())
#    commercial_id = Column(Integer, ForeignKey('commercials.idAgent'))
    user_id = Column(Integer, ForeignKey('users.idUser'))
    ordered_id = Column(Integer, ForeignKey('orders.idOrdered'))

#    commercials = relationship("Commercial", back_populates="delivers")
    users = relationship("User", back_populates="delivers")
    orders = relationship("Ordered", back_populates="delivers")
