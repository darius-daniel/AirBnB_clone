#!/usr/bin/python3
"""Contains a class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__()
