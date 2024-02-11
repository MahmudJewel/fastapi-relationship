from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ParentCreate(BaseModel):
    name: str

class Parent(ParentCreate):
    id: int

class ChildCreate(BaseModel):
    name: str
    parent_id: int

class Child(ChildCreate):
    id: int
