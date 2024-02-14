from fastapi import APIRouter
from app.api.routers.relation import relation_router

router = APIRouter()

router.include_router(relation_router)


