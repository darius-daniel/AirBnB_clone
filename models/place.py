#!/usr/bin/python3
"""Contains a class @Place that inherits from BaseModel
"""
from models.base_model import BaseModel
from models.city import City


class Place(BaseModel):
    """Represents a place object
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guests = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
