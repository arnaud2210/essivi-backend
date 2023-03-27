from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime
from settings import schemas, models
from package.tools import log_message


def get_all(db: Session):
    try:
        delivers = db.query(models.Delivery).all()
        return delivers
    except:
        return {log_message}


def create(request: schemas.Delivery, db: Session):
    try:
        new_deliver = models.Delivery(delivery_quantity=request.delivery_quantity, delivery_locations=request.delivery_locations,
                                      amount_collected=request.amount_collected, delivery_date=request.delivery_date, user_id=request.user_id, ordered_id=request.ordered_id)

        if new_deliver.delivery_quantity > 0 and new_deliver.amount_collected >= 0:
            new_deliver.ordered_date = datetime.now()
            db.add(new_deliver)
            db.commit()
            db.refresh(new_deliver)
            return new_deliver
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"******************    VEUILLEZ VERIFIER LES VALEURS SAISIES ! LA QUANTITE ET LE PRIX DOIVENT ETRE SUPERIEURE A 0  *************************")
    except:
        return {log_message}


def show_deliver(idDelivery: int, db: Session):
    deliver = db.query(models.Delivery).filter(
        models.Delivery.idDelivery == idDelivery).first()
    if not deliver:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"deliver with the id {idDelivery} doesn't exist")
    return deliver


def update(idDelivery: int, request: schemas.Ordered, db: Session):
    try:
        deliver = db.query(models.Delivery).filter(
            models.Delivery.idDelivery == idDelivery).first()

        if not deliver:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"order with the id {idDelivery} not found")

        deliver.delivery_quantity = request.delivery_quantity
        deliver.amount_collected = request.amount_collected

        if deliver.delivery_quantity > 0 and deliver.amount_collected >= 0:
            db.commit()
            return "updated"
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"******************    VEUILLEZ VERIFIER LES VALEURS SAISIES ! LA QUANTITE ET LE PRIX DOIVENT ETRE SUPERIEURE A 0  *************************")
    except:
        return {log_message}


def delete(idDelivery: int, db: Session):
    db.query(models.Delivery).filter(models.Delivery.idDelivery ==
                                     idDelivery).delete(synchronize_session=False)
    db.commit()
    return {'done'}
