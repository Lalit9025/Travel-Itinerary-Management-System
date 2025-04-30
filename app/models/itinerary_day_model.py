from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.models.base import Base

# Association tables for many-to-many relationships
day_activities = Table(
    'day_activities',
    Base.metadata,
    Column('itinerary_day_id', Integer, ForeignKey('itineraryday.id'), primary_key=True),
    Column('activity_id', Integer, ForeignKey('activity.id'), primary_key=True)
)

day_transfers = Table(
    'day_transfers',
    Base.metadata,
    Column('itinerary_day_id', Integer, ForeignKey('itineraryday.id'), primary_key=True),
    Column('transfer_id', Integer, ForeignKey('transfer.id'), primary_key=True)
)

class ItineraryDay(Base):
    """Model for individual days in an itinerary"""
    __tablename__ = "itineraryday"
    
    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey('itineraries.id'), nullable=False)
    day_number = Column(Integer, nullable=False)  # 1-based day number
    accommodation_id = Column(Integer, ForeignKey('accommodation.id'), nullable=True)
    description = Column(Text, nullable=True)
    location = Column(String(100), nullable=False)  # Current location for the day
    
    # Relationships
    itinerary = relationship("Itinerary", back_populates="days")
    accommodation = relationship("Accommodation")
    activities = relationship("Activity", secondary=day_activities)
    transfers = relationship("Transfer", secondary=day_transfers)
    
    def __repr__(self):
        return f"<ItineraryDay(day_number={self.day_number}, location='{self.location}')>"
