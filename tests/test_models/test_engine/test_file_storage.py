import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Unit tests for the FileStorage class.
    """

    def setUp(self):
        """
        Set up necessary resources for testing.
        """
        # Create a temporary file path for testing
        self.test_file_path = "test_file.json"

    def tearDown(self):
        """
        Clean up resources after testing.
        """
        # Remove the temporary file created during testing
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_initialization(self):
        """
        Test the initialization of the FileStorage class.
        """
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(storage._FileStorage__file_path, "file.json")
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_all(self):
        """
        Test the all method of the FileStorage class.
        """
        storage = FileStorage()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, storage._FileStorage__objects)

    def test_new(self):
        """
        Test the new method of the FileStorage class.
        """
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, storage._FileStorage__objects)
        self.assertEqual(storage._FileStorage__objects[key], obj)

    def test_save_and_reload(self):
        """
        Test the save and reload methods of the FileStorage class.
        """
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)

        # Save objects to the temporary file
        storage.save()

        # Create a new storage instance to simulate a program restart
        new_storage = FileStorage()
        new_storage.reload()

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, new_storage._FileStorage__objects)
        reloaded_obj = new_storage._FileStorage__objects[key]
        self.assertIsInstance(reloaded_obj, BaseModel)
        self.assertEqual(reloaded_obj.__dict__, obj.__dict__)


if __name__ == '__main__':
    unittest.main()
