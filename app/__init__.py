from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from app.db import db
from app.admin import init_admin

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_itinerary.db'  # Update with your DB URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    
    # Initialize admin interface
    init_admin(app)
    
    # Register blueprints here (if any)
    # from app.api import bp as api_bp
    # app.register_blueprint(api_bp, url_prefix='/api')
    
    return app