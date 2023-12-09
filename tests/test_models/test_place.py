import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    def setUp(self):
        # Initialize Place instance for each test
        self.place = Place()

    def test_inheritance(self):
        # Ensure Place inherits from BaseModel
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        # Ensure attributes are present and initialized with the correct values
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertEqual(self.place.city_id, "")

        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertEqual(self.place.user_id, "")

        self.assertTrue(hasattr(self.place, 'name'))
        self.assertEqual(self.place.name, "")

        self.assertTrue(hasattr(self.place, 'description'))
        self.assertEqual(self.place.description, "")

        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertEqual(self.place.number_rooms, 0)

        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertEqual(self.place.number_bathrooms, 0)

        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertEqual(self.place.max_guest, 0)

        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertEqual(self.place.price_by_night, 0)

        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertEqual(self.place.latitude, 0.0)

        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertEqual(self.place.longitude, 0.0)

        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertEqual(self.place.amenity_ids, [])

    def test_attribute_types(self):
        # Ensure attribute types are correct
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_to_dict(self):
        # Ensure to_dict method returns a dictionary with expected keys/values
        place_dict = self.place.to_dict()

        self.assertTrue(isinstance(place_dict, dict))
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)

    def test_str_representation(self):
        # Ensure __str__ method returns a string representation
        str_representation = str(self.place)

        self.assertIsInstance(str_representation, str)
        self.assertIn('Place', str_representation)


if __name__ == '__main__':
    unittest.main()
