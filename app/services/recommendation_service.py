from sqlalchemy.orm import Session
from typing import List, Optional

from app.models import Itinerary

def get_recommended_itineraries(
    db: Session,
    num_nights: int,
    region: Optional[str] = None
) -> List[Itinerary]:
    print(f"Searching for itineraries with nights={num_nights}, region={region}")
    query = db.query(Itinerary)
    
    if region:
        print(f"Filtering by region: {region}")
        query = query.filter(Itinerary.region == region)
    
    query = query.filter(Itinerary.num_nights == num_nights)
    result = query.all()
    print(f"Found {len(result)} itineraries")
    return result
