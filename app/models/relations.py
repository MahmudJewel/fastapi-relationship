from sqlalchemy import String, Column,Integer,ForeignKey, Table
from sqlalchemy.orm import relationship

from app.core.database import Base

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(225), index=True)
    classes = relationship("Class", back_populates="teacher")

class Class(Base):
    __tablename__='classes'
    id= Column(Integer,primary_key=True, index=True)
    name = Column(String(225), index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship("Teacher", back_populates="classes")

# foreignkey 
class Parent(Base):
	__tablename__ = "parents"
      
	id = Column(Integer, primary_key=True)
	name = Column(String)
	children = relationship("Child", back_populates="parent")

class Child(Base):
	__tablename__ = "children"
      
	id = Column(Integer, primary_key=True)
	name = Column(String)
	parent_id = Column(Integer, ForeignKey("parents.id"))
	parent = relationship("Parent", back_populates="children")

# Many to many relation 
association_table = Table(
	"association", Base.metadata,
	Column("employee_id", Integer, ForeignKey("employees.id")),
	Column("skill_id", Integer, ForeignKey("skills.id"))
)

class Employee(Base):
	__tablename__ = "employees"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	skill = relationship("Skill", secondary=association_table, back_populates="employee")

class Skill(Base):
	__tablename__ = "skills"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	employee = relationship("Employee", secondary=association_table, back_populates="skill")