from sqladmin import ModelView
from app.models.relations import (Parent, 
                                  Child,
                                  Employee,
                                  Skill
                                  )

class ParentAdmin(ModelView, model=Parent):
    column_list = [
        Parent.id,
        Parent.name
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