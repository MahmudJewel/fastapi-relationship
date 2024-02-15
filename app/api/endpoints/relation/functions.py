from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
# import 
from app.models import relations as RelationModel
from app.schemas.relation import (
    ParentCreate,  
    ChildCreate,
    Child,
    ParentsForChild, 
    AllEmployee,
    EmployeeCreate,
    AllSkills,
    SkillCreate
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
    query = db.query(RelationModel.Child).offset(skip).limit(limit).all()
    return query

# get all child with parent details
def read_all_child_with_parent_info(db: Session, skip: int, limit: int):
    query = db.query(RelationModel.Child, RelationModel.Parent).join(RelationModel.Parent, RelationModel.Child.parent_id== RelationModel.Parent.id).offset(skip).limit(limit).all()
    children_with_parent_info = []
    for child, parent in query:
        child_response = Child(
            id=child.id,
            name=child.name,
            parent=[ParentsForChild(id=parent.id, name=parent.name)]
        )
        children_with_parent_info.append(child_response)
    return children_with_parent_info

# =============== m2m operations ==========================
# create new employee
async def create_new_employee(db: Session, employee: EmployeeCreate):
    employee_dict = employee.model_dump() # extracting the data
    skills = employee_dict.pop('skill')
    db_employee = RelationModel.Employee(**employee_dict)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee, ["skill"]) # Employee.skill attribute will be updated with the current value stored in the corresponding database record, ensuring that you have the most up-to-date data in your object.
    if skills is not None:
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

# ================ skills =================== 
# get all skill
async def read_all_skill(db: Session, skip: int, limit: int):
    return db.query(RelationModel.Skill).offset(skip).limit(limit).all()

# get all skill with employee details
async def read_all_skill_with_employee_details(db: Session, skip: int, limit: int):
    return db.query(RelationModel.Skill).offset(skip).limit(limit).all()

# get skill by name 
def get_skill_by_name(db: Session, name: str):
    skill = db.query(RelationModel.Skill).filter(RelationModel.Skill.name == name).first()
    return skill

# create new skill
async def create_new_skill(db: Session, skill: SkillCreate):
    db_skill = get_skill_by_name(db=db, name=skill.name)
    print('Exists ==============> ', db_skill)
    if db_skill:
        raise HTTPException(status_code=404, detail="Skill already exists")
    new_skill = RelationModel.Skill(name= skill.name)
    db.add(new_skill)
    db.commit()
    db.refresh( new_skill )
    return new_skill

