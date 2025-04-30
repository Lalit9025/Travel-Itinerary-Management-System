from sqlalchemy import Column, String, Integer, Float, Text, Boolean
from app.models.base import Base

class Accommodation(Base):
    """Model for hotel accommodations"""
    name = Column(String(255), nullable=False, index=True)
    location = Column(String(100), nullable=False, index=True)  # e.g., "Phuket", "Krabi"
    address = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    rating = Column(Float, nullable=True)
    price_per_night = Column(Integer, nullable=False)  # Price in THB
    amenities = Column(Text, nullable=True)  # Comma separated list of amenities
    is_recommended = Column(Boolean, default=False)
    image_url = Column(String(255), nullable=True)
    
    def __repr__(self):
        return f"<Accommodation(name='{self.name}', location='{self.location}')>"
