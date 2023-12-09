import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def setUp(self):
        # Initialize User instance for each test
        self.user = User()

    def test_inheritance(self):
        # Ensure User inherits from BaseModel
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        # Ensure attributes are present and initialized with the correct values
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertEqual(self.user.email, "")

        self.assertTrue(hasattr(self.user, 'password'))
        self.assertEqual(self.user.password, "")

        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertEqual(self.user.first_name, "")

        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.last_name, "")

    def test_attribute_types(self):
        # Ensure attribute types are correct
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_to_dict(self):
        # Ensure to_dict method returns a dictionary with expected keys/values
        user_dict = self.user.to_dict()

        self.assertTrue(isinstance(user_dict, dict))
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)

    def test_str_representation(self):
        # Ensure __str__ method returns a string representation
        str_representation = str(self.user)

        self.assertIsInstance(str_representation, str)
        self.assertIn('User', str_representation)


if __name__ == '__main__':
    unittest.main()
