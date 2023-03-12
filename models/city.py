#!/usr/bin/python3
"""Contains a class @City that inherits from BaseModel
"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """Represents a city object
    """
    state_id = ""
    name = ""
