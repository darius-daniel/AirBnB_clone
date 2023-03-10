#!/usr/bin/python3
"""Contains a class that defines all common attributes/methods for other
classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes and methods
    """
    def __init__(self, *args, **kwargs):
        """Initializes the instance attributes for new instances
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'updated_at' or key == 'created_at':
                        form = '%Y-%m-%dT%H:%M:%S.%f'
                        setattr(self, key, datetime.strptime(value, form))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Returns the string representation of the instance of the class
        """
        cls_name = str(self.__class__.__name__)
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute @updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/valueso of @__dict__ of
        the instance
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = str(self.__class__.__name__)
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        return new_dict
