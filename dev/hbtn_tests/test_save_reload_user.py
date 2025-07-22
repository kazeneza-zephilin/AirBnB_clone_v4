#!/usr/bin/python3
"""
Unit Test for Save and Reload User
"""
import unittest
import os
from models.user import User
from models import storage


class TestSaveReloadUser(unittest.TestCase):
    """Class for testing User save and reload functionality"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Save/Reload User .....')
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

    def test_user_save_method(self):
        """Test User save method"""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        old_updated_at = user.updated_at
        user.save()
        self.assertLess(old_updated_at, user.updated_at)

    def test_user_save_to_file(self):
        """Test User save to file functionality"""
        user = User()
        user.email = "test@example.com"
        user.save()
        with open("dev/file.json", "r") as f:
            self.assertIn("User." + user.id, f.read())

    def test_user_reload_from_file(self):
        """Test User reload from file functionality"""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "Jane"
        user.last_name = "Smith"
        user.save()
        
        storage.reload()
        objects = storage.all()
        reloaded_user = objects["User." + user.id]
        
        self.assertEqual(reloaded_user.id, user.id)
        self.assertEqual(reloaded_user.email, user.email)
        self.assertEqual(reloaded_user.password, user.password)
        self.assertEqual(reloaded_user.first_name, user.first_name)
        self.assertEqual(reloaded_user.last_name, user.last_name)

    def test_user_attributes(self):
        """Test User specific attributes"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
        
        # Test default values
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
