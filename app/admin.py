from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import Accommodation, Activity, Transfer, Itinerary, ItineraryDay
from app.db import db

def init_admin(app):
    admin = Admin(app, name='Travel Itinerary Admin', template_mode='bootstrap3')
    
    # Add model views
    admin.add_view(ModelView(Accommodation, db.session))
    admin.add_view(ModelView(Activity, db.session))
    admin.add_view(ModelView(Transfer, db.session))
    admin.add_view(ModelView(Itinerary, db.session))
    admin.add_view(ModelView(ItineraryDay, db.session))