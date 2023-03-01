from sqlalchemy.orm import Session
from sqlalchemy import select, text
from fastapi import HTTPException, status
from settings import schemas, models
from package.tools import log_message


def get_all(db: Session):
    try:
        products = db.query(models.Product).all()
        return products
    except:
        return {log_message}


def create(request: schemas.Product, db: Session):
    try:
        new_product = models.Product(labelOfProduct=request.labelOfProduct,
                                     unitPrice=request.unitPrice, productQuantity=request.productQuantity, category_id=request.category_id)
        if new_product.productQuantity >= 0 and new_product.unitPrice > 0:
            db.add(new_product)
            db.commit()
            db.refresh(new_product)
            return new_product
        else:
            return print("******************    VEUILLEZ VERIFIER LES VALEURS SAISIES ! LA QUANTITE ET LE PRIX DOIVENT ETRE SUPERIEURE A 0  *************************")
    except:
        return {log_message}


def show_product(idProduct: int, db: Session):
    product = db.query(models.Product).filter(
        models.Product.idProduct == idProduct).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"product with the id {idProduct} doesn't exist")
    return product


def update(idProduct: int, request: schemas.ShowProduct, db: Session):
    try:
        product = db.query(models.Product).filter(
            models.Product.idProduct == idProduct).first()

        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Product with the id {idProduct} not found")

        product.labelOfProduct = request.labelOfProduct
        product.unitPrice = request.unitPrice
        product.productQuantity = request.productQuantity

        if product.productQuantity >= 0 and product.unitPrice > 0:
            db.commit()
            return "updated"
        else:
            return print("******************    VEUILLEZ VERIFIER LES VALEURS SAISIES ! LA QUANTITE ET LE PRIX DOIVENT ETRE SUPERIEURE A 0  *************************")
    except:
        return {log_message}


def get_details(db: Session):
    try:
        query = select([text(' * from "stock_quantity"')])
        result = db.execute(query)
        data = result.fetchall()
        return data
    except:
        return {log_message}


def delete(idProduct: int, db: Session):
    db.query(models.Product).filter(models.Product.idProduct ==
                                    idProduct).delete(synchronize_session=False)
    db.commit()
    return {'done'}
