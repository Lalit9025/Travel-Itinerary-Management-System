from pydantic import BaseModel, Field, validator, ConfigDict
from typing import List, Optional
from datetime import time, datetime
from enum import Enum

class TransportTypeEnum(str, Enum):
    CAR = "CAR"
    BUS = "BUS"
    BOAT = "BOAT"
    FERRY = "FERRY"
    PLANE = "PLANE"
    PRIVATE = "PRIVATE"
    SHARED = "SHARED"
    PUBLIC = "PUBLIC"

class ActivityCategoryEnum(str, Enum):
    ADVENTURE = "Adventure"
    SIGHTSEEING = "Sightseeing"
    BEACH = "Beach"
    CULTURAL = "Cultural"
    FOOD = "Food"
    SHOPPING = "Shopping"
    RELAXATION = "Relaxation"

class RegionEnum(str, Enum):
    PHUKET = "Phuket"
    KRABI = "Krabi"
    PHUKET_KRABI = "Phuket & Krabi"

class AccommodationBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    location: RegionEnum
    address: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    rating: Optional[float] = Field(None, ge=0, le=5)
    price_per_night: int = Field(..., gt=0)
    amenities: Optional[str] = None
    is_recommended: bool = False
    image_url: Optional[str] = None

    @validator('rating')
    def validate_rating(cls, v):
        if v is not None:
            return round(v, 1)
        return v

class ActivityBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    location: RegionEnum
    description: str = Field(..., min_length=1)
    duration_hours: float = Field(..., gt=0)
    price: int = Field(..., gt=0)
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    is_recommended: bool = False
    category: ActivityCategoryEnum
    image_url: Optional[str] = None

    @validator('end_time')
    def validate_times(cls, v, values):
        if 'start_time' in values and v is not None and values['start_time'] is not None:
            if v <= values['start_time']:
                raise ValueError('end_time must be after start_time')
        return v

class TransferBase(BaseModel):
    source: str = Field(..., min_length=1, max_length=100)
    destination: str = Field(..., min_length=1, max_length=100)
    transport_type: TransportTypeEnum
    duration_minutes: int = Field(..., gt=0)
    price: int = Field(..., gt=0)
    description: Optional[str] = None

class ItineraryDayBase(BaseModel):
    day_number: int = Field(..., gt=0)
    description: Optional[str] = None
    location: RegionEnum
    accommodation_id: Optional[int] = None
    activity_ids: List[int] = []
    transfer_ids: List[int] = []

    @validator('day_number')
    def validate_day_number(cls, v):
        if v > 31:  # Assuming maximum 31 days in a month
            raise ValueError('day_number must be less than or equal to 31')
        return v

class ItineraryDaySchema(ItineraryDayBase):
    id: int
    accommodation: Optional[AccommodationBase] = None
    activities: List[ActivityBase] = []
    transfers: List[TransferBase] = []
    
    model_config = ConfigDict(from_attributes=True)

class ItineraryBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    num_nights: int = Field(..., ge=1, le=31)  # Assuming maximum 31 nights
    total_price: int = Field(..., gt=0)
    is_recommended: bool = False
    region: RegionEnum
    days: List[ItineraryDayBase]

    @validator('days')
    def validate_days(cls, v, values):
        if 'num_nights' in values:
            if len(v) != values['num_nights']:
                raise ValueError('Number of days must match num_nights')
            
            # Check day numbers are sequential and start from 1
            day_numbers = [day.day_number for day in v]
            if sorted(day_numbers) != list(range(1, len(v) + 1)):
                raise ValueError('Day numbers must be sequential starting from 1')
        return v

class ItinerarySchema(ItineraryBase):
    id: int
    days: List[ItineraryDaySchema]
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ItineraryCreate(ItineraryBase):
    model_config = ConfigDict(from_attributes=True)

class ItineraryResponse(BaseModel):
    itinerary: ItinerarySchema
    
    model_config = ConfigDict(from_attributes=True)

# Alias for Itinerary
Itinerary = ItineraryResponse 