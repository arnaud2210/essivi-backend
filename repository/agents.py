"""from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from hashing import pass_Context
import models
import schemas


def get_all(db: Session):
    agents = db.query(models.Commercial).all()
    return agents


def create(request: schemas.Commercial, db: Session):
    new_agent = models.Commercial(firstnameOfAgent=request.firstnameOfAgent, lastnameOfAgent=request.lastnameOfAgent,
                                  addressOfAgent=request.addressOfAgent, agentPhone=request.agentPhone, agentState=request.agentState)
    db.add(new_agent)
    db.commit()
    db.refresh(new_agent)
    return new_agent


def show_agent(idAgent: int, db: Session):
    agent = db.query(models.Commercial).filter(
        models.Commercial.idAgent == idAgent).first()
    if not agent:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Agent with the id {idAgent} doesn't exist")
    return agent


def delete(idAgent: int, db: Session):
    db.query(models.Commercial).filter(models.Commercial.idAgent ==
                                       idAgent).delete(synchronize_session=False)
    db.commit()
    return {'done'}"""
