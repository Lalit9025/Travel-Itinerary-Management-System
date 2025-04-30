from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.mcp.server import app as mcp_app

# --- SQLAdmin imports ---
from sqladmin import Admin, ModelView
from app.db.db import engine  # Adjust this import to your actual engine location
from app.models import Accommodation, Activity, Transfer, Itinerary, ItineraryDay

app = FastAPI(
    title="Travel Itinerary Management System",
    description="API for managing travel itineraries in Thailand",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_router, prefix="/api/v1")
app.mount("/mcp", mcp_app)  # Mount the MCP app

# --- SQLAdmin setup ---
admin = Admin(app, engine)

class AccommodationAdmin(ModelView, model=Accommodation):
    column_list = [c.name for c in Accommodation.__table__.columns]

class ActivityAdmin(ModelView, model=Activity):
    column_list = [c.name for c in Activity.__table__.columns]

class TransferAdmin(ModelView, model=Transfer):
    column_list = [c.name for c in Transfer.__table__.columns]

class ItineraryAdmin(ModelView, model=Itinerary):
    column_list = [c.name for c in Itinerary.__table__.columns]

class ItineraryDayAdmin(ModelView, model=ItineraryDay):
    column_list = [c.name for c in ItineraryDay.__table__.columns]

admin.add_view(AccommodationAdmin)
admin.add_view(ActivityAdmin)
admin.add_view(TransferAdmin)
admin.add_view(ItineraryAdmin)
admin.add_view(ItineraryDayAdmin)

@app.get("/")
def read_root():
    return {"message": "Welcome to Travel Itinerary API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)