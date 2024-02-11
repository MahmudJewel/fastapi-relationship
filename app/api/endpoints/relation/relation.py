# fastapi 
from fastapi import APIRouter, Depends, HTTPException

# sqlalchemy
from sqlalchemy.orm import Session

# import
from app.core.dependencies import get_db, oauth2_scheme 
from app.schemas.relation import ParentCreate, Parent, ChildCreate, Child
from app.api.endpoints.relation import functions as relation_functions

relation_module = APIRouter()

# create new parents 
@relation_module.post('/', response_model=Parent)
async def create_new_parent(parent: ParentCreate, db: Session = Depends(get_db)):
    new_parent = relation_functions.create_new_parent(db, parent)
    return new_parent

# get all parents list
@relation_module.get('/', 
            response_model=list[Parent],
            # dependencies=[Depends(RoleChecker(['admin']))]
            )
async def read_all_parents( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return relation_functions.read_all_parents(db, skip, limit)


