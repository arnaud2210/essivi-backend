from sqlalchemy.orm import Session
from sqlalchemy import select, text
from fastapi import HTTPException, status
from package.tools import log_message


def caPerMonth(db: Session):
    try:
        query = select([text(' * from "chiffrePerMonth"')])
        result = db.execute(query)
        data = result.fetchall()
        return data
    except:
        return {log_message}


def caOfCatPerMonth(db: Session):
    try:
        query = select([text(' * from "chiffreCatPerMonth"')])
        result = db.execute(query)
        data = result.fetchall()
        return data
    except:
        return {log_message}


def numCustomPerAgent(db: Session):
    try:
        query = select([text(' * from "nombreClientParAgent"')])
        result = db.execute(query)
        data = result.fetchall()
        return data
    except:
        return {log_message}


def user_type(db: Session):
    try:
        query = select([text(' * from "typePersonnel"')])
        result = db.execute(query)
        data = result.fetchall()
        return data
    except:
        return {log_message}


def quantityPerCat(db: Session):
    try:
        query = select([text(' * from "quantiteParCategorie"')])
        result = db.execute(query)
        data = result.fetchall()
        return data
    except:
        return {log_message}
