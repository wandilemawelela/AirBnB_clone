import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def setUp(self):
        # Initialize Amenity instance for each test
        self.amenity = Amenity()

    def test_inheritance(self):
        # Ensure Amenity inherits from BaseModel
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        # Ensure 'name' attribute is present and initialized as an empty string
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")

    def test_attribute_types(self):
        # Ensure attribute types are correct
        self.assertIsInstance(self.amenity.name, str)

    def test_to_dict(self):
        # Ensure to_dict method returns a dictionary with expected keys/values
        amenity_dict = self.amenity.to_dict()

        self.assertTrue(isinstance(amenity_dict, dict))
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)

    def test_str_representation(self):
        # Ensure __str__ method returns a string representation
        str_representation = str(self.amenity)

        self.assertIsInstance(str_representation, str)
        self.assertIn('Amenity', str_representation)


if __name__ == '__main__':
    unittest.main()
