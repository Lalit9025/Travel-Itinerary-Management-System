# from fastapi import APIRouter, Depends, Query, FastAPI
# from sqlalchemy.orm import Session
# from typing import List, Optional
# from fastapi_mcp import FastApiMCP

# from app.db.database import get_db
# from app.services.recommendation_service import get_recommended_itineraries
# from app.schemas import ItinerarySchema

# # Create router for recommendations
# recommendations_router = APIRouter()

# @recommendations_router.get("/recommendations", response_model=List[ItinerarySchema])
# def recommend_itineraries(
#     nights: int = Query(..., description="Number of nights for the itinerary"),
#     region: Optional[str] = Query(None, description="Specific region (Phuket, Krabi, or both)"),
#     db: Session = Depends(get_db)
# ):
#     """
#     MCP endpoint that returns recommended itineraries based on the requested number of nights
#     and optionally filtered by region.
#     """
#     return get_recommended_itineraries(db=db, num_nights=nights, region=region)

# # Create FastAPI app
# app = FastAPI(
#     title="Travel Itinerary MCP Server",
#     description="Provides recommended travel itineraries based on user preferences.",
#     version="1.0.0"
# )

# # Include the recommendations router
# app.include_router(recommendations_router)

# # Initialize MCP
# mcp = FastApiMCP(
#     app,
#     name="Travel Itinerary MCP",
#     description="MCP server for travel itinerary recommendations."
# )

# # Mount MCP and expose router
# mcp.mount()
# router = app.router
# from fastapi import FastAPI, APIRouter, Depends, Query, HTTPException
# from fastapi_mcp import FastApiMCP
# from sqlalchemy.orm import Session
# from typing import List, Optional

# from app.db.database import get_db
# from app.schemas import ItinerarySchema
# from app.services.recommendation_service import get_recommended_itineraries

# # Initialize FastAPI app
# app = FastAPI(
#     title="Travel Itinerary MCP Server",
#     description="Provides recommended travel itineraries based on user preferences.",
#     version="1.0.0"
# )

# # Initialize MCP wrapper
# mcp = FastApiMCP(
#     app=app,
#     name="Travel Itinerary MCP",
#     description="MCP server for travel itinerary recommendations."
# )

# # Define router
# recommendations_router = APIRouter()


# # MCP-compliant exposed endpoint
# @mcp.expose()
# @recommendations_router.get(
#     "/recommendations",
#     response_model=List[ItinerarySchema],
#     tags=["MCP"]
# )
# def recommend_itineraries(
#     nights: int = Query(..., description="Number of nights for the itinerary"),
#     region: Optional[str] = Query(None, description="Specific region (Phuket, Krabi, or both)"),
#     db: Session = Depends(get_db)
# ):
#     """
#     MCP endpoint that returns recommended itineraries based on number of nights and optional region filter.
#     """
#     return get_recommended_itineraries(db=db, num_nights=nights, region=region)


# # Include router in FastAPI app
# app.include_router(recommendations_router)

# # Mount MCP server
# mcp.mount()

# # Expose app router if needed (optional, not required for functionality)
# router = app.router
# app/mcp/server.py
from fastapi import FastAPI, APIRouter, Depends, Query
from fastapi_mcp import FastApiMCP
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.database import get_db
from app.schemas import ItinerarySchema
from app.services.recommendation_service import get_recommended_itineraries

app = FastAPI(
    title="Travel MCP Server",
    description="Provides itinerary recommendations",
    version="1.0.0"
)

mcp = FastApiMCP(
    app,
    name="Travel MCP",
    description="MCP server for travel itinerary recommendations"
)
mcp.mount()

router = APIRouter()

@router.get("/recommendations", response_model=List[ItinerarySchema], tags=["MCP"])
def recommend_itineraries(
    nights: int = Query(...),
    region: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    response = get_recommended_itineraries(db=db, num_nights=nights, region=region)
    if not response:
        print("Warning: Empty response received from get_recommended_itineraries")
    return response

app.include_router(router)
