from sqlalchemy import Column, String, Integer, Float, Text, Boolean, Time
from app.models.base import Base

class Activity(Base):
    """Model for activities/excursions"""
    name = Column(String(255), nullable=False, index=True)
    location = Column(String(100), nullable=False, index=True)  # e.g., "Phuket", "Krabi"
    description = Column(Text, nullable=False)
    duration_hours = Column(Float, nullable=False)  # Duration in hours
    price = Column(Integer, nullable=False)  # Price in THB
    start_time = Column(Time, nullable=True)  # Optional start time
    end_time = Column(Time, nullable=True)  # Optional end time
    is_recommended = Column(Boolean, default=False)
    category = Column(String(100), nullable=True, index=True)  # e.g., "Adventure", "Cultural", "Beach"
    image_url = Column(String(255), nullable=True)
    
    def __repr__(self):
        return f"<Activity(name='{self.name}', location='{self.location}')>"
