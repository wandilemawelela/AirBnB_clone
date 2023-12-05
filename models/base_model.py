import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        """
        The following module initializes a new instance of BaseModel with
        a unique ID, creation timestamp, and the last update timestamp.
        """
        self.id = str(uuid.uuid4())  # Generate a unique ID using uuid4 and convert to string
        self.created_at = datetime.now()  # Set creation timestamp to current datetime
        self.updated_at = datetime.now()  # Set update timestamp to current datetime

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the last update timestamp to the current datetime.
        """
        self.updated_at = datetime.now()

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
