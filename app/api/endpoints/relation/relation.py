# fastapi 
from fastapi import APIRouter, Depends, HTTPException

# sqlalchemy
from sqlalchemy.orm import Session

# import
from app.core.dependencies import get_db, oauth2_scheme 
from app.schemas.relation import (
    ParentCreate, 
    Parent, 
    ChildCreate, 
    Child,
    AllEmployee,
    EmployeeCreate,
    AllSkills,
    SkillCreate
    )
from app.api.endpoints.relation import functions as relation_functions

relation_module = APIRouter()


# ================== foreign key operation ===========================

# create new parents 
@relation_module.post('/parents', response_model=Parent)
async def create_new_parent(parent: ParentCreate, db: Session = Depends(get_db)):
    new_parent = relation_functions.create_new_parent(db, parent)
    return new_parent

# get all parents list
@relation_module.get('/parents', 
            response_model=list[Parent],
            # dependencies=[Depends(RoleChecker(['admin']))]
            )
async def read_all_parents( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return relation_functions.read_all_parents(db, skip, limit)

# create new child 
@relation_module.post('/child', response_model=Child)
async def create_new_child(child: ChildCreate, db: Session = Depends(get_db)):
    new_child = relation_functions.create_new_child(db, child)
    return new_child

# get all child list
@relation_module.get('/child', 
            response_model=list[Child],
            # dependencies=[Depends(RoleChecker(['admin']))]
            )
async def read_all_child( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return relation_functions.read_all_child(db, skip, limit)

# ===================== many2many operation ==================
# create new employee 
@relation_module.post('/employee', response_model=AllEmployee)
async def create_new_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = relation_functions.create_new_employee(db, employee)
    return new_employee

# get all employee list
@relation_module.get('/employee', 
            response_model=list[AllEmployee],
            # dependencies=[Depends(RoleChecker(['admin']))]
            )
async def read_all_employee( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return relation_functions.read_all_employee(db, skip, limit)

# get all skill list
@relation_module.get('/skill', 
            response_model=list[AllSkills],
            # dependencies=[Depends(RoleChecker(['admin']))]
            )
async def read_all_employee( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return relation_functions.read_all_skill(db, skip, limit)
