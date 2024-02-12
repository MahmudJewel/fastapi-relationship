from fastapi import HTTPException, status, Depends
from typing import Annotated
from datetime import datetime, timedelta, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

# import 
from app.models import relations as RelationModel
from app.schemas.relation import (
    ParentCreate,  
    ChildCreate, 
    AllEmployee,
    AllSkills
    )
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

# =============== m2m operations ==========================
# create new employee
async def create_new_employee(db: Session, employee: AllEmployee):
    employee_dict = employee.model_dump() # extracting th data
    skills = employee_dict.pop('skill')
    db_employee = RelationModel.Employee(**employee_dict)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee, ["skill"]) # Employee.skill attribute will be updated with the current value stored in the corresponding database record, ensuring that you have the most up-to-date data in your object.
    for skill in skills:
        # print('skills =========> ', skill['name'])
        query = select(RelationModel.Skill).where(RelationModel.Skill.name == skill['name'])
        db_skill = (db.execute(query)).scalar_one_or_none() # it will return one value or none
        if db_skill is None:
            db_skill = RelationModel.Skill(name=skill['name'])
            db.add(db_skill)
        db_employee.skill.append(db_skill)
    db.commit()
    return db_employee

# get all employee
def read_all_employee(db: Session, skip: int, limit: int):
    return db.query(RelationModel.Employee).offset(skip).limit(limit).all()

# get all skill
def read_all_skill(db: Session, skip: int, limit: int):
    return db.query(RelationModel.Skill).offset(skip).limit(limit).all()

