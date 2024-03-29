from pydantic import BaseModel
from typing import Optional

# ================ One to one relation =================
class UserCreate(BaseModel):
	name: str

class VisforUser(BaseModel):
	id: int
	name: str
class User(BaseModel):
	id: int
	name: str
	visa: Optional[VisforUser]

# ================ foreign keys =================
class ParentCreate(BaseModel):
	name: str

class ChildForParents(BaseModel):
	id: int
	name: str

class Parent(ParentCreate):
	id: int
	children: list[ChildForParents] | None = None

class ChildCreate(BaseModel):
	name: str
	parent_id: int | None = None

class ParentsForChild(BaseModel):
	id: int
	name: str

class Child(BaseModel):
	id: int
	name: str | None = None
	parent: Optional[ParentsForChild]


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

class SkillCreate(EmployeeBase):
	pass

class EmployeeForSkill(BaseModel):
	id: int
	name: str

class AllSkills(BaseModel):
	id: int
	name: str
	employee: list[EmployeeForSkill]

class AllSkillsWithoutEmployee(EmployeeForSkill):
	pass