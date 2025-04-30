import os
import sys

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base
from app.models.itinerary_model import Itinerary
from app.models.itinerary_day_model import ItineraryDay, day_activities, day_transfers

# Create engine with SQLite database URL
DATABASE_URL = "sqlite:///travel_itinerary.db"
engine = create_engine(DATABASE_URL)

def reset_database():
    try:
        # Drop all tables
        Base.metadata.drop_all(engine)
        print("Dropped all existing tables.")

        # Create all tables
        Base.metadata.create_all(engine)
        print("Created all tables successfully!")
        
        return True
    except Exception as e:
        print(f"Error resetting database: {str(e)}")
        return False

if __name__ == "__main__":
    reset_database() 