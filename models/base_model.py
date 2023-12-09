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
        Initializes an object with its attributes.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Notes:
            Excludes certain attributes (e.g., '__class__', 'created_at',
            'updated_at') from initialization.

        Raises:
            ValueError: If invalid datetime format is provided.
        """
        if kwargs:
            for key, value in kwargs.items():
                # Exclude certain attributes from initialization
                if key in ['__class__', 'created_at', 'updated_at']:
                    continue

                # Convert string to datetime for 'created_at' and 'updated_at'
                if key == "created_at" or key == "updated_at":
                    try:
                        value = datetime.fromisoformat(value) if value else None
                    except ValueError:
                        raise ValueError(f"Invalid datetime format "
                                         f"for {key}: {value}")

                # Set attribute
                setattr(self, key, value)

        else:
            # Initialize new object with default values
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            # Save the new object
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
        Returns the string representation
        of the instance.

        Returns:
            str: String representation of the instance.
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, vars(self))

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime.
        Saves the object.

        Notes:
            Make sure to call this method after making changes to the object.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.

        Returns:
            dict: Dictionary representation of the instance.
        """
        obj_dict = vars(self).copy()
        obj_dict['__class__'] = type(self).__name__

        # Convert created_at and updated_at to ISO format
        for attr in ['created_at', 'updated_at']:
            if attr in obj_dict and obj_dict[attr]:
                obj_dict[attr] = obj_dict[attr].isoformat()

        return obj_dict
