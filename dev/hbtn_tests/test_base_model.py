#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class for testing BaseModel"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing BaseModel .....')
        print('.................................\n\n')

    def setUp(self):
        """Set up test methods"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Tear down test methods"""
        del self.base_model

    def test_init(self):
        """Test BaseModel initialization"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_str(self):
        """Test BaseModel string representation"""
        string = str(self.base_model)
        self.assertIn(self.base_model.__class__.__name__, string)
        self.assertIn(self.base_model.id, string)

    def test_save(self):
        """Test BaseModel save method"""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_json(self):
        """Test BaseModel to_json method"""
        json_dict = self.base_model.to_json()
        self.assertIsInstance(json_dict, dict)
        self.assertEqual(json_dict['__class__'], 'BaseModel')
        self.assertEqual(json_dict['id'], self.base_model.id)


if __name__ == '__main__':
    unittest.main()
