#!/usr/bin/python3
"""
Unit Test for Storage get and count methods
"""
import unittest
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.review import Review


class TestGetCount(unittest.TestCase):
    """Class for testing storage get and count methods"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Get/Count .....')
        print('.................................\n\n')

    def test_get_method(self):
        """Test storage get method"""
        # Create a test state
        state = State(name="Test State")
        state.save()
        
        # Test get method
        retrieved_state = storage.get(State, state.id)
        self.assertEqual(retrieved_state.id, state.id)
        self.assertEqual(retrieved_state.name, state.name)
        
        # Test get with invalid id
        invalid_state = storage.get(State, "invalid-id")
        self.assertIsNone(invalid_state)
        
        # Clean up
        storage.delete(state)

    def test_count_method(self):
        """Test storage count method"""
        # Count all objects
        initial_count = storage.count()
        self.assertIsInstance(initial_count, int)
        
        # Count specific class
        state_count = storage.count(State)
        self.assertIsInstance(state_count, int)
        
        # Create new object and test count increase
        new_state = State(name="Count Test State")
        new_state.save()
        
        new_count = storage.count()
        new_state_count = storage.count(State)
        
        self.assertEqual(new_count, initial_count + 1)
        self.assertEqual(new_state_count, state_count + 1)
        
        # Clean up
        storage.delete(new_state)


if __name__ == '__main__':
    unittest.main()
