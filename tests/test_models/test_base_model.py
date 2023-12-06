<<<<<<< HEAD
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
=======
import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """
        Set up a new BaseModel instance for testing.
        """
        self.base_model = BaseModel()

    def test_init(self):
        """
        Test the initialization of BaseModel.
        """
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        """
        Test the __str__ method of BaseModel.
        """
        expected_output = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_output)

    def test_save(self):
        """
        Test the save method of BaseModel.
        """
        initial_updated_at = self.base_model.updated_at
        with patch.object(BaseModel, 'updated_at') as mock_updated_at:
            self.base_model.save()
            mock_updated_at.assert_called_once()
            self.assertNotEqual(self.base_model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        """
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        obj_dict = self.base_model.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertCountEqual(obj_dict.keys(), expected_keys)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
>>>>>>> origin/main

