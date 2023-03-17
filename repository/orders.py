from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import select, text
from datetime import datetime
from settings import schemas, models
from package.tools import log_message


def get_all(db: Session):
    try:
        orders = db.query(models.Ordered).order_by(
            models.Ordered.idOrdered.desc()).all()
        return orders
    except:
        return {log_message}


def create(request: schemas.Ordered, db: Session):
    try:
        new_order = models.Ordered(ordered_quantity=request.ordered_quantity, ordered_date=request.ordered_date,
                                   customer_id=request.customer_id, product_id=request.product_id)
        if new_order.ordered_quantity > 0:
            new_order.ordered_date = datetime.now()
            db.add(new_order)
            db.commit()
            db.refresh(new_order)
            return new_order
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"******************    VEUILLEZ VERIFIER LES VALEURS SAISIES ! LA QUANTITE DOIT ETRE SUPERIEURE A 0   *************************")
    except:
        return {log_message}


def show_order(idOrdered: int, db: Session):
    order = db.query(models.Ordered).filter(
        models.Ordered.idOrdered == idOrdered).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"order with the id {idOrdered} doesn't exist")
    return order


def update(idOrder: int, request: schemas.Ordered, db: Session):
    try:
        order = db.query(models.Ordered).filter(
            models.Ordered.idOrdered == idOrder).first()

        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"order with the id {idOrder} not found")

        order.ordered_quantity = request.ordered_quantity
        order.product_id = request.product_id

        if order.ordered_quantity > 0:
            db.commit()
            return "updated"
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"******************    VEUILLEZ VERIFIER LES VALEURS SAISIES ! LA QUANTITE DOIT ETRE SUPERIEURE A 0   *************************")
    except:
        return {log_message}


def delete(idOrdered: int, db: Session):
    db.query(models.Ordered).filter(models.Ordered.idOrdered ==
                                    idOrdered).delete(synchronize_session=False)
    db.commit()
    return {'done'}


def orders_not_delivered(db: Session):
    try:
        query = select([text(' * from "ordersNotDelivered"')])
        result = db.execute(query)
        data = result.fetchall()
        return data
    except:
        return {log_message}
