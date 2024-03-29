# fastapi 
from fastapi import APIRouter, Depends
# sqlalchemy
from sqlalchemy.orm import Session
# import
from app.core.dependencies import get_db 
from app.schemas.relation import (
    ParentCreate, 
    Parent, 
    ChildCreate, 
    Child,
    AllEmployee,
    EmployeeCreate,
    AllSkills,
    AllSkillsWithoutEmployee,
    SkillCreate,
    User,
    UserCreate
    )
from app.api.endpoints.relation import functions as relation_functions

one2one_module = APIRouter()
many2one_module = APIRouter()
many2many_module = APIRouter()


# ================== One to one relation ===========================
# create new user 
@one2one_module.post('/user', response_model=User)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = relation_functions.create_new_user(db, user)
    return new_user

# get all user list
@one2one_module.get('/user', 
            response_model=list[User],
            # dependencies=[Depends(RoleChecker(['admin']))]
            )
async def read_all_users( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return relation_functions.read_all_users(db, skip, limit)

# # create new child 
# @one2one_module.post('/child', response_model=Child)
# async def create_new_child(child: ChildCreate, db: Session = Depends(get_db)):
#     new_child = relation_functions.create_new_child(db, child)
#     return new_child

# # get all child list
# @one2one_module.get('/child', 
#             # response_model=list[Child],
#             # dependencies=[Depends(RoleChecker(['admin']))]
#             )
# async def read_all_child( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
#     return relation_functions.read_all_child(db, skip, limit)

# @one2one_module.get('/child-with-parents-info', 
#             response_model=list[Child],
#             # dependencies=[Depends(RoleChecker(['admin']))]
#             )
# async def read_all_child_with_parent_info( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
#     return relation_functions.read_all_child_with_parent_info(db, skip, limit)

# ================== foreign key operation ===========================
# create new parents 
@many2one_module.post('/parents', response_model=Parent)
async def create_new_parent(parent: ParentCreate, db: Session = Depends(get_db)):
    new_parent = relation_functions.create_new_parent(db, parent)
    return new_parent

# get all parents list
@many2one_module.get('/parents', 
            response_model=list[Parent],
            # dependencies=[Depends(RoleChecker(['admin']))]
            )
async def read_all_parents( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return relation_functions.read_all_parents(db, skip, limit)

# create new child 
@many2one_module.post('/child', response_model=Child)
async def create_new_child(child: ChildCreate, db: Session = Depends(get_db)):
    new_child = relation_functions.create_new_child(db, child)
    return new_child

# get all child list
@many2one_module.get('/child', 
            # response_model=list[Child],
            # dependencies=[Depends(RoleChecker(['admin']))]
            )
async def read_all_child( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return relation_functions.read_all_child(db, skip, limit)

@many2one_module.get('/child-with-parents-info', 
            response_model=list[Child],
            # dependencies=[Depends(RoleChecker(['admin']))]
            )
async def read_all_child_with_parent_info( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return relation_functions.read_all_child_with_parent_info(db, skip, limit)


# ===================== many2many operation ==================
# create new employee 
@many2many_module.post('/employee', 
                      response_model=AllEmployee
                      )
async def create_new_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = await relation_functions.create_new_employee(db, employee)
    return new_employee

# get all employee list
@many2many_module.get('/employee', 
            response_model=list[AllEmployee],
            # dependencies=[Depends(RoleChecker(['admin']))]
            )
async def read_all_employee( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return relation_functions.read_all_employee(db, skip, limit)

# get all skill list
@many2many_module.get('/skill', 
            response_model=list[AllSkillsWithoutEmployee],
            )
async def read_all_skill( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return await relation_functions.read_all_skill(db, skip, limit)

# get all skill with employee details
@many2many_module.get('/skill-with-employee-details', 
            response_model=list[AllSkills],
            )
async def read_all_skill_with_employee_details( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return await relation_functions.read_all_skill_with_employee_details(db, skip, limit)

# create new employee 
@many2many_module.post('/skill', 
                      response_model=AllSkillsWithoutEmployee
                      )
async def create_new_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    new_skill = await relation_functions.create_new_skill(db, skill)
    return new_skill
