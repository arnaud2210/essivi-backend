"""from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from repository import agents
from hashing import pass_Context
from database import get_db_connect
from oauth2 import get_current_user
from typing import List
import schemas
import models


router = APIRouter(
    prefix="/agents",
    tags=['Agents']
)


@router.post('/', response_model=schemas.ShowAgent)
def create_agent(request: schemas.Commercial, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return agents.create(request, db)


@router.get('/{id}', response_model=schemas.ShowAgent)
def get_agent(idAgent: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return agents.show_agent(idAgent, db)


@router.get('/', response_model=List[schemas.ShowAgent])
def get_agents(db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return agents.get_all(db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_agent(idAgent: int, db: Session = Depends(get_db_connect), current_user: schemas.User = Depends(get_current_user)):
    return agents.delete(idAgent, db)"""
