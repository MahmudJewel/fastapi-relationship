from sqlalchemy import String, Column,Integer,ForeignKey
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

