from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.core.database import get_db
from app.services import itinerary_service
from app.schemas.validation import ItineraryCreate, Itinerary as ItinerarySchema
from app.core.exceptions import (
    ItineraryNotFound, AccommodationNotFound, ActivityNotFound,
    TransferNotFound, DatabaseError, ValidationError
)

router = APIRouter()

@router.post("/", response_model=ItinerarySchema)
def create_itinerary(
    itinerary: ItineraryCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new itinerary
    """
    try:
        created_itinerary = itinerary_service.create_itinerary(db, itinerary)
        return {"itinerary": created_itinerary}
    except (AccommodationNotFound, ActivityNotFound, TransferNotFound) as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{itinerary_id}", response_model=ItinerarySchema)
def read_itinerary(
    itinerary_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific itinerary by ID
    """
    try:
        itinerary = itinerary_service.get_itinerary(db, itinerary_id)
        return {"itinerary": itinerary}
    except ItineraryNotFound as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[ItinerarySchema])
def list_itineraries(
    skip: int = 0,
    limit: int = 100,
    region: Optional[str] = None,
    nights: Optional[int] = None,
    is_recommended: bool = False,
    db: Session = Depends(get_db)
):
    """
    List itineraries with optional filtering
    """
    try:
        itineraries = itinerary_service.list_itineraries(
            db,
            skip=skip,
            limit=limit,
            region=region,
            nights=nights,
            is_recommended=is_recommended
        )
        return [{"itinerary": itinerary} for itinerary in itineraries]
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e)) 