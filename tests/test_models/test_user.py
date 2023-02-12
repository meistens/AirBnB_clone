#!/usr/bin/python3
"""Modules needed for state class test"""
import unittest
import pycodestyle
from models.user import User


class State_test(unittest.TestCase):
    """test class for user class"""
    def test_doc(self):
        """checks if documentation exists for user"""
        docs = User.__init__.__doc__
        self.assertGreater(len(docs), 1)

    def test_str_format(self):
        """Tests the __str__ is correct"""
        strFormat = User()
        str_format = "[User] ({}) {}".format(strFormat.id, strFormat.__dict__)
        self.assertEqual(str_format, str(strFormat))

    def test_user(self):
        """Tests if state just works"""
        foo = User()
        self.assertEqual(type(foo).__name__, "User")

    def test_name_attrs(self):
        """Tests if user instance has a name attribute, and it is empty"""
        foo = User()
        self.assertEqual(type(foo).__name__, "User")
        self.assertTrue(hasattr(foo, "id"))
        self.assertTrue(hasattr(foo, "created_at"))
        self.assertTrue(hasattr(foo, "updated_at"))
        self.assertTrue(hasattr(foo, "__class__"))
