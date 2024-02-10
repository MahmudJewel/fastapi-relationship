# fastapi 
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from typing import List

# sqlalchemy
from sqladmin import Admin, ModelView

# import 
from app.core.database import engine
from app.models.admin import (UserAdmin, 
                              TeacherAdmin, 
                              ClassAdmin, 
                              ParentAdmin, 
                              ChildAdmin,
                              EmployeeAdmin,
                              SkillAdmin
                              )
from app.api.routers.api import router
# from app.core.settings import config

def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)
    # admin dashboard 
    admin = Admin(app_, engine)
    admin.add_view(UserAdmin)
    admin.add_view(TeacherAdmin)
    admin.add_view(ClassAdmin)
    admin.add_view(ParentAdmin)
    admin.add_view(ChildAdmin)
    admin.add_view(EmployeeAdmin)
    admin.add_view(SkillAdmin)


origins = [
    "*",
	# "http://localhost.tiangolo.com",
	# "https://localhost.tiangolo.com",
	# "http://localhost",
	# "http://localhost:8080",
]

def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        # Middleware(SQLAlchemyMiddleware),
    ]
    return middleware