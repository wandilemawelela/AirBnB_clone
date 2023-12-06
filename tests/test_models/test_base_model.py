import unittest
from datetime import datetime
from unittest.mock import patch, PropertyMock
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

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

    def test_init_with_kwargs(self):
        """
        Test initialization with kwargs.
        """
        data = {
            'id': '123',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-02T12:00:00.000000',
            'custom_attribute': 'value'
        }
        instance = BaseModel(**data)

        self.assertEqual(instance.id, '123')
        self.assertEqual(instance.custom_attribute, 'value')
        self.assertEqual(
            instance.created_at,
            datetime.strptime('2022-01-01T12:00:00.000000', '%Y-%m-%dT%H:%M:%S.%f')
        )
        self.assertEqual(
            instance.updated_at,
            datetime.strptime('2022-01-02T12:00:00.000000', '%Y-%m-%dT%H:%M:%S.%f')
        )

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
        with patch.object(self.base_model, 'updated_at') as mock_updated_at:
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

    def test_to_dict_with_custom_attribute(self):
        """
        Test to_dict method with a custom attribute.
        """
        self.base_model.custom_attribute = 'value'
        obj_dict = self.base_model.to_dict()

        self.assertIn('custom_attribute', obj_dict)
        self.assertEqual(obj_dict['custom_attribute'], 'value')

if __name__ == '__main__':
    unittest.main()

