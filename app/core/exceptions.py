from fastapi import HTTPException, status
from typing import Any, Dict, Optional

class TravelItineraryException(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: str,
        headers: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class ItineraryNotFound(TravelItineraryException):
    def __init__(self, itinerary_id: int) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Itinerary with id {itinerary_id} not found"
        )

class AccommodationNotFound(TravelItineraryException):
    def __init__(self, accommodation_id: int) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Accommodation with id {accommodation_id} not found"
        )

class ActivityNotFound(TravelItineraryException):
    def __init__(self, activity_id: int) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Activity with id {activity_id} not found"
        )

class TransferNotFound(TravelItineraryException):
    def __init__(self, transfer_id: int) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transfer with id {transfer_id} not found"
        )

class InvalidItineraryData(TravelItineraryException):
    def __init__(self, detail: str) -> None:
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )

class DatabaseError(TravelItineraryException):
    def __init__(self, detail: str) -> None:
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {detail}"
        )

class ValidationError(TravelItineraryException):
    def __init__(self, detail: str) -> None:
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail
        )

class RecommendationError(TravelItineraryException):
    def __init__(self, detail: str) -> None:
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Recommendation error: {detail}"
        ) 