import uuid
from datetime import datetime

try:
    from models.engine.file_storage import storage  # Try to import storage
except ImportError:
    storage = None  # Handle ImportError gracefully

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            *args: Additional arguments.
            **kwargs: Additional keyword arguments. If provided, updates attributes based on kwargs.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())  # Generate a unique ID using uuid4
            self.created_at = datetime.now()  # Creation timestamp to the current datetime
            self.updated_at = datetime.now()  # Update timestamp to the current datetime

            # If it’s a new instance (not from a dictionary representation),
            # add a call to the method new(self) on storage
            if storage:
                storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the last update timestamp to the current datetime.
        Calls the save method of storage.
        """
        if storage:
            self.updated_at = datetime.now()
            storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance for serialization.

        Returns:
            dict: A dictionary containing the object's attributes.
        """
        obj_dict = self.__dict__.copy()  # Create a copy of the instance dictionary
        obj_dict['__class__'] = self.__class__.__name__  # Add the class name to the dictionary
        obj_dict['created_at'] = self.created_at.isoformat()  # Convert created_at to ISO format
        obj_dict['updated_at'] = self.updated_at.isoformat()  # Convert updated_at to ISO format
        return obj_dict

