# Travel Itinerary Management System

**Objective**  
Developed a full-stack backend system using **FastAPI** and **SQLAlchemy** to manage travel itineraries, including trip creation, retrieval, and MCP-based itinerary recommendations.

---

## Steps Followed

### 1. Database Modeling
- Designed SQLAlchemy ORM models for **Itinerary**, **Day**, **Accommodation**, **Activity**, and **Transfer** with appropriate relationships and constraints.

### 2. Schema Design
- *Itinerary* supports day-wise plans with relations to activities, transfers, and accommodations.
- Ensured normalized schema with indexes on:
  - `region`
  - `num_nights`
  - `is_recommended`

### 3. Seeding
- Populated schema with realistic data for **Phuket** and **Krabi** including recommended trips (2–8 nights), activities (e.g., Phi Phi tour, cooking class), and transfers.

### 4. API Implementation
Created RESTful endpoints with **FastAPI**:

- `POST /api/v1/itineraries/` - Create a new itinerary.
- `GET /api/v1/itineraries/` - Retrieve all itineraries.
- `GET /api/v1/itineraries/{itinerary_id}` - Retrieve a specific itinerary by ID with error handling.

---

## Key Decisions

- **Day-wise modular schema**: Facilitates easy itinerary customization and extension.
- **Nested request models**: Allow clients to submit complete itineraries with nested days and linked activities/transfers.

---

## Assumptions

- An itinerary can have multiple activities/transfers per day.
- Times and prices can be `null` for optional fields (e.g., `start_time`).
- Activities and transfers are reusable entities shared across itineraries.

---

## Project Setup

### Clone the Repository
```bash
git clone https://github.com/Lalit9025/Travel-Itinerary-Management-System.git
```

### Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Environment Configuration
Create a `.env` file in the root directory:
```
DATABASE_URL=sqlite:///./travel_itinerary.db
SECRET_KEY=your secret
DEBUG=True
```

---

## Initialize Database
Create database and tables and seed initial data:
```bash
python -m app.db.db
```

---

## Running the Application
Start the server:
```bash
uvicorn app.main:app --reload
```

