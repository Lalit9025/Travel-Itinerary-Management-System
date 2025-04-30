from sqlalchemy import Column, String, Integer, Float, Text, Enum
import enum
from app.models.base import Base

class TransportType(enum.Enum):
    """Enum for transport types"""
    CAR = "CAR"
    BUS = "BUS"
    BOAT = "BOAT"
    FERRY = "FERRY"
    PLANE = "PLANE"

class Transfer(Base):
    """Model for transfers between locations"""
    source = Column(String(100), nullable=False, index=True)  # Starting location
    destination = Column(String(100), nullable=False, index=True)  # End location
    transport_type = Column(Enum(TransportType), nullable=False)
    duration_minutes = Column(Integer, nullable=False)  # Duration in minutes
    price = Column(Integer, nullable=False)  # Price in THB
    description = Column(Text, nullable=True)
    
    def __repr__(self):
        return f"<Transfer(source='{self.source}', destination='{self.destination}', type='{self.transport_type.value}')>"
