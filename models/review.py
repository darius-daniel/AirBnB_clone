#!/usr/bin/python3
"""Contains a class @Review that inherits from BaseModel
"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place


class Review(BaseModel):
    """Represents a review object
    """
    place_id = ""
    user_id = ""
    text = ""
