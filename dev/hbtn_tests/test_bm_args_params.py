#!/usr/bin/python3
"""
Unit Test for BaseModel with Args and Params
"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBMArgsParams(unittest.TestCase):
    """Class for testing BaseModel with various arguments and parameters"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing BM Args/Params .....')
        print('.................................\n\n')

    def test_args_unused(self):
        """Test that args are not used in BaseModel"""
        base_model = BaseModel(None, 1, "test")
        self.assertNotIn(None, base_model.__dict__.values())
        self.assertNotIn(1, base_model.__dict__.values())
        self.assertNotIn("test", base_model.__dict__.values())

    def test_kwargs_instantiation(self):
        """Test BaseModel instantiation with kwargs"""
        dt = datetime.datetime.now()
        dt_iso = dt.isoformat()
        base_model = BaseModel(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(base_model.id, "123")
        self.assertEqual(base_model.created_at, dt)
        self.assertEqual(base_model.updated_at, dt)

    def test_kwargs_none(self):
        """Test BaseModel with None kwargs"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_args_and_kwargs(self):
        """Test BaseModel with both args and kwargs"""
        dt = datetime.datetime.now()
        dt_iso = dt.isoformat()
        base_model = BaseModel("unused", id="123", created_at=dt_iso)
        self.assertEqual(base_model.id, "123")
        self.assertEqual(base_model.created_at, dt)

    def test_kwargs_with_class(self):
        """Test kwargs with __class__ key"""
        dt = datetime.datetime.now()
        dt_iso = dt.isoformat()
        base_model = BaseModel(id="123", created_at=dt_iso, __class__="BaseModel")
        self.assertEqual(base_model.id, "123")
        self.assertNotIn("__class__", base_model.__dict__)


if __name__ == '__main__':
    unittest.main()
