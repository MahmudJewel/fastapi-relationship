from fastapi import APIRouter
from app.api.endpoints.relation.relation import relation_module
# from app.api.endpoints.user.auth import auth_module

relation_router = APIRouter()

relation_router.include_router(
    relation_module,
    prefix="/relation",
    tags=["Relationship"],
    responses={404: {"description": "Not found"}},
)

# user_router.include_router(
#     auth_module,
#     prefix="",
#     tags=["auth"],
#     responses={404: {"description": "Not found"}},
# )