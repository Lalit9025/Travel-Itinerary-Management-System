import os
import random
from sqlalchemy.orm import Session
from app.models import (
    Accommodation,
    Activity,
    Transfer,
    Itinerary,
    ItineraryDay,
)
from app.db.database import SessionLocal, engine
from app.models.base import Base
import enum

class TransportType(enum.Enum):
    """Enum for transport types"""
    CAR = "CAR"
    BUS = "BUS"
    BOAT = "BOAT"
    FERRY = "FERRY"
    PLANE = "PLANE"

def seed_accommodations(db: Session):
    """Seed accommodations for Phuket and Krabi"""
    
    # Phuket Accommodations
    phuket_accommodations = [
        {
            "name": "Anantara Mai Khao Phuket Villas",
            "location": "Phuket",
            "address": "888 Moo 3, Mai Khao, Thalang, Phuket 83110",
            "description": "Luxury pool villas nestled in tropical gardens near Mai Khao Beach.",
            "rating": 4.8,
            "price_per_night": 12000,
            "amenities": "Private pool, Spa, Beachfront, Restaurant, Free WiFi",
            "is_recommended": True,
            "image_url": "anantara_mai_khao.jpg"
        },
        {
            "name": "The Shore at Katathani",
            "location": "Phuket",
            "address": "14 Kata Noi Road, Karon, Muang, Phuket 83100",
            "description": "Adult-only luxury resort with private pool villas overlooking Kata Noi Beach.",
            "rating": 4.7,
            "price_per_night": 15000,
            "amenities": "Private infinity pool, Ocean view, Spa, Restaurant, Free WiFi",
            "is_recommended": True,
            "image_url": "shore_katathani.jpg"
        },
        {
            "name": "The Slate",
            "location": "Phuket",
            "address": "116 Moo 1, Sakhu, Thalang, Phuket 83110",
            "description": "Unique design resort inspired by Phuket's tin mining past.",
            "rating": 4.6,
            "price_per_night": 8000,
            "amenities": "Multiple pools, Spa, Restaurants, Free WiFi, Fitness center",
            "is_recommended": True,
            "image_url": "the_slate.jpg"
        },
        {
            "name": "Patong Beach Hotel",
            "location": "Phuket",
            "address": "124 Taweewong Road, Patong, Kathu, Phuket 83150",
            "description": "Centrally located hotel in the heart of Patong's entertainment district.",
            "rating": 4.0,
            "price_per_night": 3500,
            "amenities": "Swimming pool, Restaurant, Bar, Free WiFi",
            "is_recommended": False,
            "image_url": "patong_beach_hotel.jpg"
        },
    ]
    
    # Krabi Accommodations
    krabi_accommodations = [
        {
            "name": "Rayavadee",
            "location": "Krabi",
            "address": "214 Moo 2, Tumbon Ao-Nang, Amphur Muang, Krabi 81000",
            "description": "Luxury resort set on the edge of Krabi Marine National Park.",
            "rating": 4.9,
            "price_per_night": 18000,
            "amenities": "Beachfront, Multiple restaurants, Spa, Free WiFi, Water sports",
            "is_recommended": True,
            "image_url": "rayavadee.jpg"
        },
        {
            "name": "Pimalai Resort & Spa",
            "location": "Krabi",
            "address": "99 Moo 5, Ba Kan Tieng Beach, Koh Lanta, Krabi 81150",
            "description": "Elegant beachfront resort on Koh Lanta with stunning Andaman Sea views.",
            "rating": 4.8,
            "price_per_night": 14000,
            "amenities": "Infinity pools, Beachfront, Spa, Multiple restaurants, Free WiFi",
            "is_recommended": True,
            "image_url": "pimalai.jpg"
        },
        {
            "name": "Railay Bay Resort & Spa",
            "location": "Krabi",
            "address": "145 Moo 2, Ao Nang, Muang, Krabi 81000",
            "description": "Beach resort located on the stunning Railay Peninsula.",
            "rating": 4.5,
            "price_per_night": 6500,
            "amenities": "Beachfront, Swimming pools, Spa, Restaurant, Free WiFi",
            "is_recommended": True,
            "image_url": "railay_bay.jpg"
        },
        {
            "name": "Aonang Cliff Beach Resort",
            "location": "Krabi",
            "address": "328 Moo 2, Ao Nang, Muang, Krabi 81000",
            "description": "Modern resort with panoramic views of Ao Nang Bay.",
            "rating": 4.3,
            "price_per_night": 4500,
            "amenities": "Infinity pool, Restaurants, Spa, Fitness center, Free WiFi",
            "is_recommended": False,
            "image_url": "aonang_cliff.jpg"
        },
    ]
    
    # Add all accommodations to database
    for acc_data in phuket_accommodations + krabi_accommodations:
        db_acc = Accommodation(**acc_data)
        db.add(db_acc)
    
    db.commit()
    print("Seeded accommodations")

def seed_activities(db: Session):
    """Seed activities for Phuket and Krabi"""
    
    # Phuket Activities
    phuket_activities = [
        {
            "name": "Phi Phi Islands Tour",
            "location": "Phuket",
            "description": "Full-day speedboat tour to the stunning Phi Phi Islands including Maya Bay and Monkey Beach.",
            "duration_hours": 8.0,
            "price": 2500,
            "start_time": None,
            "end_time": None,
            "is_recommended": True,
            "category": "Adventure",
            "image_url": "phi_phi_tour.jpg"
        },
        {
            "name": "Old Phuket Town Walking Tour",
            "location": "Phuket",
            "description": "Explore the charming streets of Old Phuket Town with its Sino-Portuguese architecture and local history.",
            "duration_hours": 3.0,
            "price": 800,
            "start_time": None,
            "end_time": None,
            "is_recommended": True,
            "category": "Cultural",
            "image_url": "phuket_town.jpg"
        },
        {
            "name": "Phang Nga Bay Sea Canoe",
            "location": "Phuket",
            "description": "Paddle through hidden lagoons and limestone caves in the dramatic Phang Nga Bay.",
            "duration_hours": 7.0,
            "price": 3200,
            "start_time": None,
            "end_time": None,
            "is_recommended": True,
            "category": "Adventure",
            "image_url": "phang_nga_canoe.jpg"
        },
        {
            "name": "Thai Cooking Class",
            "location": "Phuket",
            "description": "Learn to cook authentic Thai dishes with a professional chef in a traditional setting.",
            "duration_hours": 4.0,
            "price": 1800,
            "start_time": None,
            "end_time": None,
            "is_recommended": False,
            "category": "Food",
            "image_url": "thai_cooking.jpg"
        },
    ]
    
    # Krabi Activities
    krabi_activities = [
        {
            "name": "Four Islands Tour",
            "location": "Krabi",
            "description": "Visit four stunning islands: Chicken Island, Tup Island, Poda Island, and Phra Nang Cave Beach.",
            "duration_hours": 6.0,
            "price": 1800,
            "start_time": None,
            "end_time": None,
            "is_recommended": True,
            "category": "Adventure",
            "image_url": "four_islands.jpg"
        },
        {
            "name": "Hot Springs and Emerald Pool",
            "location": "Krabi",
            "description": "Relax in natural hot springs and swim in the crystal-clear Emerald Pool in the jungle.",
            "duration_hours": 7.0,
            "price": 1500,
            "start_time": None,
            "end_time": None,
            "is_recommended": True,
            "category": "Relaxation",
            "image_url": "emerald_pool.jpg"
        },
        {
            "name": "Rock Climbing at Railay",
            "location": "Krabi",
            "description": "Rock climbing lesson on Railay's world-famous limestone cliffs for all skill levels.",
            "duration_hours": 4.0,
            "price": 2000,
            "start_time": None,
            "end_time": None,
            "is_recommended": True,
            "category": "Adventure",
            "image_url": "railay_climbing.jpg"
        },
        {
            "name": "Kayaking in Ao Thalane",
            "location": "Krabi",
            "description": "Paddle through mangrove forests and explore hidden lagoons in Ao Thalane.",
            "duration_hours": 4.0,
            "price": 1200,
            "start_time": None,
            "end_time": None,
            "is_recommended": False,
            "category": "Adventure",
            "image_url": "ao_thalane.jpg"
        },
    ]
    
    # Add all activities to database
    for act_data in phuket_activities + krabi_activities:
        db_act = Activity(**act_data)
        db.add(db_act)
    
    db.commit()
    print("Seeded activities")

def seed_transfers(db: Session):
    """Seed transfers between locations"""
    
    transfers = [
        {
            "source": "Phuket Airport",
            "destination": "Patong Beach",
            "transport_type": TransportType.CAR.value,
            "duration_minutes": 45,
            "price": 800,
            "description": "Private car transfer from Phuket Airport to Patong Beach hotels."
        },
        {
            "source": "Phuket Airport",
            "destination": "Kata Beach",
            "transport_type": TransportType.CAR.value,
            "duration_minutes": 60,
            "price": 1000,
            "description": "Private car transfer from Phuket Airport to Kata Beach hotels."
        },
        {
            "source": "Phuket",
            "destination": "Krabi",
            "transport_type": TransportType.BUS.value,
            "duration_minutes": 180,
            "price": 300,
            "description": "Air-conditioned van transfer between Phuket and Krabi."
        },
        {
            "source": "Phuket",
            "destination": "Phi Phi Islands",
            "transport_type": TransportType.FERRY.value,
            "duration_minutes": 120,
            "price": 600,
            "description": "Ferry transfer from Phuket to Phi Phi Islands."
        },
        {
            "source": "Krabi Airport",
            "destination": "Ao Nang",
            "transport_type": TransportType.CAR.value,
            "duration_minutes": 30,
            "price": 600,
            "description": "Private car transfer from Krabi Airport to Ao Nang hotels."
        },
        {
            "source": "Ao Nang",
            "destination": "Railay Beach",
            "transport_type": TransportType.BOAT.value,
            "duration_minutes": 15,
            "price": 200,
            "description": "Longtail boat transfer from Ao Nang to Railay Beach."
        },
        {
            "source": "Krabi",
            "destination": "Koh Lanta",
            "transport_type": TransportType.FERRY.value,
            "duration_minutes": 90,
            "price": 400,
            "description": "Ferry transfer from Krabi mainland to Koh Lanta."
        },
    ]
    
    for transfer_data in transfers:
        db_transfer = Transfer(**transfer_data)
        db.add(db_transfer)
    
    db.commit()
    print("Seeded transfers")

def create_sample_itineraries(db: Session):
    """Create sample recommended itineraries"""
    
    # Get all seeded data
    accommodations = {
        "Phuket": db.query(Accommodation).filter(Accommodation.location == "Phuket").all(),
        "Krabi": db.query(Accommodation).filter(Accommodation.location == "Krabi").all()
    }
    
    activities = {
        "Phuket": db.query(Activity).filter(Activity.location == "Phuket").all(),
        "Krabi": db.query(Activity).filter(Activity.location == "Krabi").all()
    }
    
    transfers = db.query(Transfer).all()
    
    # Create a 3-night Phuket itinerary
    phuket_3_night = Itinerary(
        title="Phuket Discovery - 3 Nights",
        description="Experience the best of Phuket with beaches, culture, and adventure.",
        num_nights=3,
        total_price=35000,
        is_recommended=True,
        region="Phuket"
    )
    db.add(phuket_3_night)
    db.flush()
    
    # Day 1
    day1 = ItineraryDay(
        itinerary_id=phuket_3_night.id,
        day_number=1,
        location="Phuket",
        description="Arrival and relaxation",
        accommodation_id=accommodations["Phuket"][0].id
    )
    airport_transfer = next((t for t in transfers if t.source == "Phuket Airport" and t.destination == "Patong Beach"), None)
    if airport_transfer:
        day1.transfers.append(airport_transfer)
    db.add(day1)
    
    # Day 2
    day2 = ItineraryDay(
        itinerary_id=phuket_3_night.id,
        day_number=2,
        location="Phuket",
        description="Island exploration",
        accommodation_id=accommodations["Phuket"][0].id
    )
    day2.activities.append(activities["Phuket"][0])  # Phi Phi Tour
    db.add(day2)
    
    # Day 3
    day3 = ItineraryDay(
        itinerary_id=phuket_3_night.id,
        day_number=3,
        location="Phuket",
        description="Culture and cuisine",
        accommodation_id=accommodations["Phuket"][0].id
    )
    day3.activities.append(activities["Phuket"][1])  # Old Town Tour
    day3.activities.append(activities["Phuket"][3])  # Cooking Class
    db.add(day3)
    
    # Day 4 (Departure)
    day4 = ItineraryDay(
        itinerary_id=phuket_3_night.id,
        day_number=4,
        location="Phuket",
        description="Departure day",
        accommodation_id=None
    )
    db.add(day4)
    
    # Create a 5-night Phuket & Krabi itinerary
    combined_5_night = Itinerary(
        title="Phuket & Krabi Explorer - 5 Nights",
        description="The perfect combination of Phuket's vibrant atmosphere and Krabi's natural beauty.",
        num_nights=5,
        total_price=65000,
        is_recommended=True,
        region="Phuket & Krabi"
    )
    db.add(combined_5_night)
    db.flush()
    
    # Day 1
    day1 = ItineraryDay(
        itinerary_id=combined_5_night.id,
        day_number=1,
        location="Phuket",
        description="Arrival in Phuket",
        accommodation_id=accommodations["Phuket"][1].id
    )
    airport_transfer = next((t for t in transfers if t.source == "Phuket Airport"), None)
    if airport_transfer:
        day1.transfers.append(airport_transfer)
    db.add(day1)
    
    # Day 2
    day2 = ItineraryDay(
        itinerary_id=combined_5_night.id,
        day_number=2,
        location="Phuket",
        description="Phuket exploration day",
        accommodation_id=accommodations["Phuket"][1].id
    )
    day2.activities.append(activities["Phuket"][2])  # Phang Nga Bay
    db.add(day2)
    
    # Day 3
    day3 = ItineraryDay(
        itinerary_id=combined_5_night.id,
        day_number=3,
        location="Krabi",
        description="Transfer to Krabi",
        accommodation_id=accommodations["Krabi"][0].id
    )
    phuket_to_krabi = next((t for t in transfers if t.source == "Phuket" and t.destination == "Krabi"), None)
    if phuket_to_krabi:
        day3.transfers.append(phuket_to_krabi)
    db.add(day3)
    
    # Day 4
    day4 = ItineraryDay(
        itinerary_id=combined_5_night.id,
        day_number=4,
        location="Krabi",
        description="Island hopping in Krabi",
        accommodation_id=accommodations["Krabi"][0].id
    )
    day4.activities.append(activities["Krabi"][0])  # Four Islands Tour
    db.add(day4)
    
    # Day 5
    day5 = ItineraryDay(
        itinerary_id=combined_5_night.id,
        day_number=5,
        location="Krabi",
        description="Adventure day in Krabi",
        accommodation_id=accommodations["Krabi"][0].id
    )
    day5.activities.append(activities["Krabi"][2])  # Rock Climbing
    db.add(day5)
    
    # Day 6 (Departure)
    day6 = ItineraryDay(
        itinerary_id=combined_5_night.id,
        day_number=6,
        location="Krabi",
        description="Departure day",
        accommodation_id=None
    )
    db.add(day6)
    
    # Create a 7-night comprehensive itinerary
    comprehensive_7_night = Itinerary(
        title="Thailand Beach Paradise - 7 Nights",
        description="Complete Thailand beach experience with the best of Phuket and Krabi.",
        num_nights=7,
        total_price=90000,
        is_recommended=True,
        region="Phuket & Krabi"
    )
    db.add(comprehensive_7_night)
    db.flush()
    
    # Days for 7-night itinerary
    for day_num in range(1, 9):  # 1 to 8 (7 nights + departure day)
        location = "Phuket" if day_num <= 4 else "Krabi"
        accommodation_id = accommodations[location][0].id if day_num < 8 else None
        
        description = f"Day {day_num}: "
        if day_num == 1:
            description += "Arrival in Phuket"
        elif day_num == 4:
            description += "Transfer to Krabi"
        elif day_num == 8:
            description += "Departure day"
            accommodation_id = None
        else:
            description += f"{location} exploration day"
        
        day = ItineraryDay(
            itinerary_id=comprehensive_7_night.id,
            day_number=day_num,
            location=location,
            description=description,
            accommodation_id=accommodation_id
        )
        
        # Add transfers as needed
        if day_num == 1:
            airport_transfer = next((t for t in transfers if t.source == "Phuket Airport"), None)
            if airport_transfer:
                day.transfers.append(airport_transfer)
        elif day_num == 4:
            phuket_to_krabi = next((t for t in transfers if t.source == "Phuket" and t.destination == "Krabi"), None)
            if phuket_to_krabi:
                day.transfers.append(phuket_to_krabi)
        
        # Add activities
        if location == "Phuket" and 1 < day_num < 4:
            # Add some Phuket activities
            day.activities.append(random.choice(activities["Phuket"]))
        elif location == "Krabi" and 4 < day_num < 8:
            # Add some Krabi activities
            day.activities.append(random.choice(activities["Krabi"]))
        
        db.add(day)
    
    db.commit()
    print("Seeded itineraries")

def seed_database():
    """Main function to seed all data"""
    # Create DB session
    db = SessionLocal()
    
    # Drop all tables
    Base.metadata.drop_all(bind=engine)

    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    try:
        # Seed data
        seed_accommodations(db)
        seed_activities(db)
        seed_transfers(db)
        create_sample_itineraries(db)
        
        print("Database seeded successfully!")
    except Exception as e:
        print(f"Error seeding database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()