from fastapi import APIRouter
from app.api.endpoints.relation.relation import many2one_module, many2many_module
# from app.api.endpoints.user.auth import auth_module

relation_router = APIRouter()

relation_router.include_router(
    many2one_module,
    prefix="/relation",
    tags=["Foreignkey"],
    responses={404: {"description": "Not found"}},
)

relation_router.include_router(
    many2many_module,
    prefix="/relation",
    tags=["Many to Many relation"],
    responses={404: {"description": "Not found"}},
)