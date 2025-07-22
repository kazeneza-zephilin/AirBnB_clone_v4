#!/usr/bin/python3
"""
Unit Test for BaseModel Dictionary Functionality
"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModelDict(unittest.TestCase):
    """Class for testing BaseModel dictionary functionality"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing BaseModel Dict .....')
        print('.................................\n\n')

    def test_to_json_type(self):
        """Test to_json returns dictionary"""
        base_model = BaseModel()
        json_dict = base_model.to_json()
        self.assertEqual(type(json_dict), dict)

    def test_to_json_class_name(self):
        """Test to_json contains class name"""
        base_model = BaseModel()
        json_dict = base_model.to_json()
        self.assertEqual(json_dict["__class__"], "BaseModel")

    def test_to_json_datetime_format(self):
        """Test to_json datetime format"""
        base_model = BaseModel()
        json_dict = base_model.to_json()
        created_at = json_dict["created_at"]
        self.assertEqual(type(created_at), str)

    def test_kwargs_instantiation(self):
        """Test BaseModel instantiation with kwargs"""
        base_model = BaseModel()
        json_dict = base_model.to_json()
        new_model = BaseModel(**json_dict)
        self.assertEqual(new_model.id, base_model.id)
        self.assertEqual(new_model.created_at, base_model.created_at)
        self.assertEqual(new_model.updated_at, base_model.updated_at)


if __name__ == '__main__':
    unittest.main()
