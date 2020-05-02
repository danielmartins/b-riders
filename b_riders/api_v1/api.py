from fastapi import APIRouter

from b_riders.api_v1.endpoints import rides, login, classification

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(classification.router, prefix="/classification", tags=["rides"])
api_router.include_router(rides.router, prefix="/rides", tags=["rides"])
