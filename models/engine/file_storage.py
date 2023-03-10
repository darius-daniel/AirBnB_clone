#!/usr/bin/python3
"""Contains a class thet serializes instances to a JSON file and deserializes
JSON file to instances
"""
import json
import os


class FileStorage:
    """Serializes instances to JSON file and deserialize JSON file to
    instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary @__objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in @__objects the obj with key <obj class name>.id

        Args:
            obj: the new object to be added to @__objects
        """
        key = str(obj.__class__.__name__) + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes @__objects to JSON file
        """
        dct = {}

        for key, value in FileStorage.__objects.items():
            dct[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(dct, file)

    def reload(self):
        """Deserializes JSON file to @__objects if the JSON file exist.
        Otherwise, do nothing and raise no exceptions
        """
        from models.base_model import BaseModel

        cls_dct = {'BaseModel': BaseModel}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                for item in json.load(file).values():
                    new_obj = cls_dct[item['__class__']](**item)
                    self.new(new_obj)
