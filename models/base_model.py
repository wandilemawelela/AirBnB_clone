import uuid
from datetime import datetime

class BaseModel:
<<<<<<< HEAD
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
=======
    def __init__(self, *args, **kwargs):
        """
        The following module initializes a new instance of BaseModel with
        a unique ID, creation timestamp, and the last update timestamp.
        If kwargs is not empty, updates attributes based on kwargs.
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
            self.created_at = datetime.now()  # Creation timestamp to current datetime
            self.updated_at = datetime.now()  # Update timestamp to currentdatetime

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
>>>>>>> origin/main
        return obj_dict
