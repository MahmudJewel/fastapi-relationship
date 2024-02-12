from sqlalchemy import String, Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.database import Base


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(225), index=True)
    classes = relationship("Class", back_populates="teacher")


class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(225), index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship("Teacher", back_populates="classes")


# ==================== foreignkey =================
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
    name = Column(String)
    employee = relationship(
        "Employee", secondary=employee_skill, back_populates="skill"
    )

    def __repr__(self):
        return f"{self.name}"
    
# association_table = Table(
#     "association_table",
#     Base.metadata,
#     Column("left_id", ForeignKey("left_table.id"), primary_key=True),
#     Column("right_id", ForeignKey("right_table.id"), primary_key=True),
# )


# class Parent2(Base):
#     __tablename__ = "left_table"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     children: Mapped[List[Child]] = relationship(
#         secondary=association_table, back_populates="parents"
#     )


# class Child2(Base):
#     __tablename__ = "right_table"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     parents: Mapped[List[Parent]] = relationship(
#         secondary=association_table, back_populates="children"
#     )

