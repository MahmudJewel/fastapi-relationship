from sqladmin import ModelView
from app.models.user import User
from app.models.relations import (Parent, 
                                  Child, 
                                  Teacher,
                                  Class,
                                  Employee,
                                  Skill
                                  )

class UserAdmin(ModelView, model=User):
    column_list = [
        User.id,
        User.first_name,
        User.last_name,
        User.email,
        User.password,
        User.is_active,
        User.role,
        User.created_at,
        User.updated_at,
    ]

class TeacherAdmin(ModelView, model=Teacher):
    column_list = [
        Teacher.id,
        Teacher.name
        # Teacher.is_active,
        # Teacher.created_at,
        # Teacher.updated_at,
    ]

class ClassAdmin(ModelView, model=Class):
    column_list = [
        Class.id,
        Class.name,
        Class.teacher_id
        # Teacher.is_active,
        # Teacher.created_at,
        # Teacher.updated_at,
    ]

class ParentAdmin(ModelView, model=Parent):
    column_list = [
        Parent.id,
        Parent.name,
        # Teacher.is_active,
        # Teacher.created_at,
        # Teacher.updated_at,
    ]

class ChildAdmin(ModelView, model=Child):
    column_list = [
        Child.id,
        Child.name,
        Child.parent_id
        # Teacher.is_active,
        # Teacher.created_at,
        # Teacher.updated_at,
    ]
class EmployeeAdmin(ModelView, model=Employee):
    column_list = [
        Employee.id,
        Employee.name,
        # Employee.skill_id
        # Teacher.is_active,
        # Teacher.created_at,
        # Teacher.updated_at,
    ]
class SkillAdmin(ModelView, model=Skill):
    column_list = [
        Skill.id,
        Skill.name,
        # Skill.employee_id
        # Teacher.is_active,
        # Teacher.created_at,
        # Teacher.updated_at,
    ]