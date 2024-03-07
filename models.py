from datetime import datetime

from config import app, db


class Human(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(30), index=True, unique=False)
    sec_name: str = db.Column(db.String(50), index=True, unique=False)
    photo: str = db.Column(db.String(1500), index=True, unique=False)
    gender: str = db.Column(db.String(10), index=True, unique=False)
    age: int = db.Column(db.String(3), index=True, unique=False)
    country: str = db.Column(db.String(50), index=True, unique=False)
    bio: str = db.Column(db.String(10000), index=True, unique=False)
    datetime: str = db.Column(db.DateTime, default=datetime.utcnow)

class Flat(db.Model):
    price = db.Column(db.Integer, primary_key=True)
    condition : str = db.Column(db.String(30), index=True, unique=False)
    furniture : str = db.Column(db.String(30), index=True, unique=False)
    city: str = db.Column(db.String(30), index=True, unique=False)
    district: str = db.Column(db.String(30), index=True, unique=False)
    type_buildings_of_house: str = db.Column(db.String(30), index=True, unique=False)
    rooms:  int = db.Column(db.String(3), index=True, unique=False)
    floor:  int = db.Column(db.String(3), index=True, unique=False)

