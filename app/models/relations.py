from sqlalchemy import String, Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.core.database import Base

# ==================== One to One relation =================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # visa_id = Column(Integer, ForeignKey('visas.id'))
    visa = relationship("Visa", uselist=False, back_populates="user")
    # uselist=False means that each User has only one Visa, and it is not represented as a list.

    def __repr__(self):
        return f"{self.name}"
class Visa(Base):
    __tablename__ = "visas"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    visa_number = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    user = relationship("User", back_populates="visa")

    def __repr__(self):
        return f"{self.name}"


# ==================== foreignkey =================
class Parent(Base):
    __tablename__ = "parents"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    children = relationship("Child", back_populates="parent")

    def __repr__(self):
        return f"{self.name}"


class Child(Base):
    __tablename__ = "children"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("parents.id"))
    parent = relationship("Parent", back_populates="children")

    def __repr__(self):
        return f"{self.name}"


# ================ Many to many relation ===========================
employee_skill = Table(
    "employee_skill",
    Base.metadata,
    Column("employee_id", Integer, ForeignKey("employees.id")),
    Column("skill_id", Integer, ForeignKey("skills.id")),
)

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    skill = relationship(
        "Skill", secondary=employee_skill, back_populates="employee"
    )

    def __repr__(self):
        return f"{self.name}"

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    employee = relationship(
        "Employee", secondary=employee_skill, back_populates="skill"
    )

    def __repr__(self):
        return f"{self.name}"
