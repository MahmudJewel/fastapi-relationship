from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from app.models.relations import Skill

# ================ foreign keys =================
class ParentCreate(BaseModel):
    name: str


class Parent(ParentCreate):
    id: int


class ChildCreate(BaseModel):
    name: str
    parent_id: int


class Child(ChildCreate):
    id: int


# ==================== many to many relations ======================

# ============== employee =================
class SkillBase(BaseModel):
    name: str
class EmployeeCreate(BaseModel):
    name: str
    skill: list[SkillBase]

class SkillForEmployee(BaseModel):
    id: int
    name: str

class AllEmployee(BaseModel):
    id: int
    name: str
    # skill: List['Skill'] = []
    skill: list[SkillForEmployee]

# ==================== skills =========================
class SkillCreate(BaseModel):
    name: str
    employee_id: list[int]

class EmployeeForSkill(BaseModel):
    id: int
    name: str
class AllSkills(BaseModel):
    id: int
    name: str
    employee: list[EmployeeForSkill]
