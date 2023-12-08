#!/usr/bin/python3
"""
Module: base.py
"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """
    Base class which defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        instatiates an object with it's
        attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ['__class__', 'created_at', 'updated_at']:
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value) if value else None
                setattr(self, key, value)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        """
        Returns the string representation
        of the instance
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, vars(self))

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        obj_dict = vars(self).copy()
        obj_dict['__class__'] = type(self).__name__
        
        # Check if created_at and updated_at exist before converting to isoformat
        if 'created_at' in obj_dict and obj_dict['created_at']:
            obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        if 'updated_at' in obj_dict and obj_dict['updated_at']:
            obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        return obj_dict


