from fastapi import HTTPException, status, Depends
from typing import Annotated
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

# import 
from app.models import relations as RelationModel
from app.schemas.relation import ParentCreate, ChildCreate
from app.core.settings import SECRET_KEY, ALGORITHM
from app.core.dependencies import get_db, oauth2_scheme


# ================== foreign key operation ===========================
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

# create new child
def create_new_child(db: Session, child: ChildCreate):
    new_child = RelationModel.Child(name=child.name, parent_id=child.parent_id )
    db.add(new_child)
    db.commit()
    db.refresh(new_child)
    return new_child

# get all child 
def read_all_child(db: Session, skip: int, limit: int):
    return db.query(RelationModel.Child).offset(skip).limit(limit).all()


