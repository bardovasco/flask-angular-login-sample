import datetime
from app import db

class User(db.Model):
    """
    User model that handles both, class
    __init__ method and provides declarative
    metadata to create an SQL User table.
    """
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(120), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    passphrase = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, nullable=False)

