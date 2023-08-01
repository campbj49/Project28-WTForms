"""Models for Adoption Center"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
    app.app_context().push()
    
    
class Pet(db.Model):
    """Pet model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False)
    species = db.Column(db.String(50),
                     nullable=False)
    photo_url = db.Column(db.String(255), nullable=True)
    
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.String(255), nullable=True)
    available = db.Column(db.Boolean, nullable = False, default = True)