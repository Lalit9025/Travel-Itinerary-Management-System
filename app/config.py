import os
from typing import Optional
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Travel Itinerary API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./travel_itinerary.db"
    
    # CORS
    BACKEND_CORS_ORIGINS: list = ["*"]  # In production, replace with specific origins
    
    class Config:
        case_sensitive = True

settings = Settings()
