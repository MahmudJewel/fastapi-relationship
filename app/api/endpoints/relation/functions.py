from fastapi import HTTPException, status, Depends
from typing import Annotated
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

# import 
from app.models import relations as RelationModel
from app.schemas.relation import ParentCreate, ChildCreate
from app.core.settings import SECRET_KEY, ALGORITHM
from app.core.dependencies import get_db, oauth2_scheme



# create new parents
def create_new_parent(db: Session, parent: ParentCreate):
    new_parent = RelationModel.Parent(name=parent.name)
    db.add(new_parent)
    db.commit()
    db.refresh(new_parent)
    return new_parent

# get all parent 
def read_all_parents(db: Session, skip: int, limit: int):
    return db.query(RelationModel.Parent).offset(skip).limit(limit).all()

