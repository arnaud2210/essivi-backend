from sqlalchemy.orm import Session
from sqlalchemy import select, text
from fastapi import HTTPException, status
from settings import schemas, models
from package.tools import log_message


def get_all(db: Session):
    try:
        customers = db.query(models.Customer).order_by(
            models.Customer.idCustomer.desc()).all()
        return customers
    except:
        return {log_message}


def create(request: schemas.Customer, db: Session):
    try:
        new_customer = models.Customer(firstnameOfCustomer=request.firstnameOfCustomer, lastnameOfCustomer=request.lastnameOfCustomer,
                                       customerPhone=request.customerPhone, longitude=request.longitude, latitude=request.latitude, user_id=request.user_id)
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
        return new_customer
    except:
        return {log_message}


def show_customer(idCustomer: int, db: Session):
    customer = db.query(models.Customer).filter(
        models.Customer.idCustomer == idCustomer).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"customer with the id {idCustomer} doesn't exist")
    return customer


def update(idCustomer: int, request: schemas.Customer, db: Session):
    try:
        customer = db.query(models.Customer).filter(
            models.Customer.idCustomer == idCustomer).first()

        if not customer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Customer with the id {idCustomer} not found")

        customer.firstnameOfCustomer = request.firstnameOfCustomer
        customer.lastnameOfCustomer = request.lastnameOfCustomer
        customer.customerPhone = request.customerPhone
        customer.longitude = request.longitude
        customer.latitude = request.latitude
        db.commit()

        return "updated"
    except:
        return {log_message}


def get_invoices(db: Session):
    try:
        query = select([text(' * from "Invoices"')])
        result = db.execute(query)
        data = result.fetchall()
        return data
    except:
        return {log_message}


# def get_invoice(idCustomer: int, db: Session):
#    query = select([text(' * from "totalInvoice"')]).where(text('"totalInvoice".idCustomer')== idCustomer)
#    result = db.execute(query)
#    data = result.fetchone()
#    return data


def delete(idCustomer: int, db: Session):
    db.query(models.Customer).filter(models.Customer.idCustomer ==
                                     idCustomer).delete(synchronize_session=False)
    db.commit()
    return {'done'}
