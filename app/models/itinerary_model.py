from sqlalchemy import Column, String, Integer, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.models.base import Base

class Itinerary(Base):
    """Model for trip itineraries"""
    __tablename__ = "itineraries"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    num_nights = Column(Integer, nullable=False, index=True)  # Number of nights
    total_price = Column(Integer, nullable=False)  # Total price in THB
    is_recommended = Column(Boolean, default=False, index=True)
    region = Column(String(100), nullable=False, index=True)  # e.g., "Phuket", "Krabi", "Phuket & Krabi"
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    days = relationship("ItineraryDay", back_populates="itinerary", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Itinerary(title='{self.title}', nights={self.num_nights}, region='{self.region}')>"
