import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def setUp(self):
        # Initialize Review instance for each test
        self.review = Review()

    def test_inheritance(self):
        # Ensure Review inherits from BaseModel
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        # Ensure attributes are present and initialized with the correct values
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertEqual(self.review.place_id, "")

        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertEqual(self.review.user_id, "")

        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.text, "")

    def test_attribute_types(self):
        # Ensure attribute types are correct
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_to_dict(self):
        # Ensure to_dict method returns a dictionary with expected keys/values
        review_dict = self.review.to_dict()

        self.assertTrue(isinstance(review_dict, dict))
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)

    def test_str_representation(self):
        # Ensure __str__ method returns a string representation
        str_representation = str(self.review)

        self.assertIsInstance(str_representation, str)
        self.assertIn('Review', str_representation)


if __name__ == '__main__':
    unittest.main()
