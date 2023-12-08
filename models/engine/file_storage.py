#!/usr/bin/python3

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    @classmethod
    def all(cls):
        """
        Returns the dictionary __objects
        """
        return cls.__objects

    @classmethod
    def new(cls, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{type(obj).__name__}.{obj.id}"
        cls.__objects[key] = obj

    @classmethod
    def save(cls):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        serialized_objects = {k: v.to_dict() for k, v in cls.__objects.items()}
        with open(cls.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    @classmethod
    def reload(cls):
        """
        Deserializes the JSON file to __objects only if the JSON
        file exists; otherwise, does nothing
        """
        current_classes = {
            'BaseModel': BaseModel, 'User': User,
            'Amenity': Amenity, 'City': City, 'State': State,
            'Place': Place, 'Review': Review
        }

        if not os.path.exists(cls.__file_path):
            return

        with open(cls.__file_path, 'r') as f:
            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                return

            cls.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()
            }
