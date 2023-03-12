#!/usr/bin/python3
"""Contains a class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a single user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
