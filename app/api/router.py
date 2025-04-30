from fastapi import APIRouter
from app.api.endpoints import itineraries

api_router = APIRouter()
api_router.include_router(itineraries.router, prefix="/itineraries", tags=["itineraries"])
