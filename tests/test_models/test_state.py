import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def setUp(self):
        # Initialize State instance for each test
        self.state = State()

    def test_inheritance(self):
        # Ensure State inherits from BaseModel
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        # Ensure 'name' attribute is present and initialized as an empty string
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")

    def test_attribute_types(self):
        # Ensure attribute types are correct
        self.assertIsInstance(self.state.name, str)

    def test_to_dict(self):
        # Ensure to_dict method returns a dictionary with expected keys/values
        state_dict = self.state.to_dict()

        self.assertTrue(isinstance(state_dict, dict))
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)

    def test_str_representation(self):
        # Ensure __str__ method returns a string representation
        str_representation = str(self.state)

        self.assertIsInstance(str_representation, str)
        self.assertIn('State', str_representation)


if __name__ == '__main__':
    unittest.main()
