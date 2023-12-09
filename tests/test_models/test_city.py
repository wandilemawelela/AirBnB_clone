import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def setUp(self):
        # Initialize City instance for each test
        self.city = City()

    def test_inheritance(self):
        # Ensure City inherits from BaseModel
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        # Ensure 'state_id' and 'name' attributes are present
        # and initialized as empty strings
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertEqual(self.city.state_id, "")

        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.name, "")

    def test_attribute_types(self):
        # Ensure attribute types are correct
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_to_dict(self):
        # Ensure to_dict method returns a dictionary with expected keys/values
        city_dict = self.city.to_dict()

        self.assertTrue(isinstance(city_dict, dict))
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)

    def test_str_representation(self):
        # Ensure __str__ method returns a string representation
        str_representation = str(self.city)

        self.assertIsInstance(str_representation, str)
        self.assertIn('City', str_representation)


if __name__ == '__main__':
    unittest.main()
