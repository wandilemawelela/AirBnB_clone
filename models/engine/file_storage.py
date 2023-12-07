"""
This module defines the FileStorage class for serializing and deserializing objects to/from a JSON file.
"""

import json
from os.path import exists
import os
from models.base_model import BaseModel

class FileStorage:
    """
    The FileStorage class handles the serialization and deserialization of objects to and from a JSON file.
    """

    # __file_path = os.path.join(os.getcwd(), "file.json")
    __file_path = "/home/tki/software-engineering/ALX/AirBnB_clone/file.json"
    __objects = {}

    def all(self):
        """
        Retrieve the dictionary of serialized objects.

        Returns:
            dict: A dictionary containing objects serialized as dictionaries.
        """

        print(f"Objects in storage: {self.__objects}") # Debug statement

        return self.__objects

    def new(self, obj):
        """
        Add a new object to the __objects dictionary.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialize and save the objects to the JSON file.
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserialize and load objects from the JSON file to __objects (if the file exists).
        """
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, obj_dict in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_class = eval(class_name)  # Convert class name to actual class
                    self.__objects[key] = obj_class(**obj_dict)
