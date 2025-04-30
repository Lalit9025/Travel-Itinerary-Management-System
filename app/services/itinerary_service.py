from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import HTTPException

from app.models import Itinerary, ItineraryDay, Accommodation, Activity, Transfer
from app.schemas.validation import ItineraryCreate
from app.core.exceptions import (
    ItineraryNotFound, AccommodationNotFound, ActivityNotFound,
    TransferNotFound, DatabaseError, ValidationError
)

def create_itinerary(db: Session, itinerary_data: ItineraryCreate) -> Itinerary:
    """
    Create a new itinerary with its days, accommodations, activities, and transfers
    """
    try:
        # Create the itinerary
        db_itinerary = Itinerary(
            title=itinerary_data.title,
            description=itinerary_data.description,
            num_nights=itinerary_data.num_nights,
            total_price=itinerary_data.total_price,
            is_recommended=itinerary_data.is_recommended,
            region=itinerary_data.region
        )
        db.add(db_itinerary)
        db.flush()  # Flush to get the itinerary ID
        
        # Create each day
        for day_data in itinerary_data.days:
            # Validate accommodation exists
            if day_data.accommodation_id:
                accommodation = db.query(Accommodation).filter(Accommodation.id == day_data.accommodation_id).first()
                if not accommodation:
                    raise AccommodationNotFound(day_data.accommodation_id)
            
            db_day = ItineraryDay(
                itinerary_id=db_itinerary.id,
                day_number=day_data.day_number,
                description=day_data.description,
                location=day_data.location,
                accommodation_id=day_data.accommodation_id
            )
            
            # Add activities
            if day_data.activity_ids:
                activities = db.query(Activity).filter(Activity.id.in_(day_data.activity_ids)).all()
                if len(activities) != len(day_data.activity_ids):
                    missing_ids = set(day_data.activity_ids) - {a.id for a in activities}
                    raise ActivityNotFound(next(iter(missing_ids)))
                db_day.activities.extend(activities)
                
            # Add transfers
            if day_data.transfer_ids:
                transfers = db.query(Transfer).filter(Transfer.id.in_(day_data.transfer_ids)).all()
                if len(transfers) != len(day_data.transfer_ids):
                    missing_ids = set(day_data.transfer_ids) - {t.id for t in transfers}
                    raise TransferNotFound(next(iter(missing_ids)))
                db_day.transfers.extend(transfers)
            
            db.add(db_day)
        
        db.commit()
        db.refresh(db_itinerary)
        return db_itinerary
        
    except (AccommodationNotFound, ActivityNotFound, TransferNotFound) as e:
        db.rollback()
        raise e
    except Exception as e:
        db.rollback()
        raise DatabaseError(str(e))

def get_itinerary(db: Session, itinerary_id: int) -> Optional[Itinerary]:
    """
    Get a specific itinerary by ID
    """
    itinerary = db.query(Itinerary).filter(Itinerary.id == itinerary_id).first()
    if not itinerary:
        raise ItineraryNotFound(itinerary_id)
    return itinerary

def list_itineraries(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    region: Optional[str] = None,
    nights: Optional[int] = None,
    is_recommended: bool = False
) -> List[Itinerary]:
    """
    List itineraries with optional filtering
    """
    try:
        query = db.query(Itinerary)
        
        if region:
            query = query.filter(Itinerary.region == region)
        
        if nights:
            query = query.filter(Itinerary.num_nights == nights)
        
        if is_recommended:
            query = query.filter(Itinerary.is_recommended == True)
        
        return query.offset(skip).limit(limit).all()
    except Exception as e:
        raise DatabaseError(str(e))
