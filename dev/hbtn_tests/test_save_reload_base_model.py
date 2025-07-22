#!/usr/bin/python3
"""
Unit Test for Save and Reload BaseModel
"""
import unittest
import os
from models.base_model import BaseModel
from models import storage


class TestSaveReloadBaseModel(unittest.TestCase):
    """Class for testing BaseModel save and reload functionality"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Save/Reload BM .....')
        print('.................................\n\n')

    def setUp(self):
        """Set up test methods"""
        try:
            os.rename("dev/file.json", "dev/file.json.bak")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Tear down test methods"""
        try:
            os.remove("dev/file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("dev/file.json.bak", "dev/file.json")
        except FileNotFoundError:
            pass

    def test_save_method(self):
        """Test BaseModel save method"""
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertLess(old_updated_at, base_model.updated_at)

    def test_save_to_file(self):
        """Test save to file functionality"""
        base_model = BaseModel()
        base_model.save()
        with open("dev/file.json", "r") as f:
            self.assertIn("BaseModel." + base_model.id, f.read())

    def test_reload_from_file(self):
        """Test reload from file functionality"""
        base_model = BaseModel()
        base_model.save()
        storage.reload()
        objects = storage.all()
        self.assertIn("BaseModel." + base_model.id, objects)

    def test_save_reload_consistency(self):
        """Test save and reload maintains data consistency"""
        base_model = BaseModel()
        base_model.name = "Test Model"
        base_model.number = 42
        base_model.save()
        
        storage.reload()
        objects = storage.all()
        reloaded_model = objects["BaseModel." + base_model.id]
        
        self.assertEqual(reloaded_model.id, base_model.id)
        self.assertEqual(reloaded_model.name, base_model.name)
        self.assertEqual(reloaded_model.number, base_model.number)


if __name__ == '__main__':
    unittest.main()
