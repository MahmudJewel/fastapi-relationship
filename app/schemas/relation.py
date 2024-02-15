from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from app.models.relations import Skill


# ================ foreign keys =================
class ParentCreate(BaseModel):
	name: str


class ChildForParents(BaseModel):
	id: int
	name: str


class Parent(ParentCreate):
	id: int
	children: list[ChildForParents] | None = None
	class Config:
		fields = {"id": "id", "name":"name", "children":"children"}


class ChildCreate(BaseModel):
	name: str
	parent_id: int | None = None


class ParentsForChild(BaseModel):
	id: int
	name: str


class Child(BaseModel):
	id: int
	name: str | None = None
	parent: list[ParentsForChild] | None = None


# ==================== many to many relations ======================


# ============== employee =================
class SkillBase(BaseModel):
	name: str


class EmployeeCreate(BaseModel):
	name: str
	skill: list[SkillBase] | None = None


class SkillForEmployee(BaseModel):
	id: int
	name: str


class AllEmployee(BaseModel):
	id: int
	name: str
	# skill: List['Skill'] = []
	skill: list[SkillForEmployee]


# ==================== skills =========================
class EmployeeBase(BaseModel):
	name: str


class SkillCreate(BaseModel):
	name: str
	employee: list[EmployeeBase] | None = None


class EmployeeForSkill(BaseModel):
	id: int
	name: str


class AllSkills(BaseModel):
	id: int
	name: str
	employee: list[EmployeeForSkill]
