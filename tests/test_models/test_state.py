#!/usr/bin/python3
"""Modules needed for state class test"""
import unittest
import pycodestyle
from models.state import State


class State_test(unittest.TestCase):
    """test class for state class"""
    def test_doc(self):
        """checks if documentation exists for state"""
        docs = State.__init__.__doc__
        self.assertGreater(len(docs), 1)

    def test_str_format(self):
        """Tests the __str__ is correct"""
        strFormat = State()
        str_format = "[State] ({}) {}".format(strFormat.id, strFormat.__dict__)
        self.assertEqual(str_format, str(strFormat))

    def test_dict(self):
        """Tests to_dict"""
        dicts = State()
        to_dict = dicts.to_dict()
        self.assertEqual(type(to_dict), dict)
        for attr in dicts.__dict__:
            self.assertTrue(attr in to_dict)

    def test_state(self):
        """Tests if state just works"""
        foo = State()
        self.assertEqual(type(foo).__name__, "State")

    def test_name_attr(self):
        """Tests if state instance has a name attribute, and it is empty"""
        foo = State()
        self.assertTrue(hasattr(foo, "name"))
        self.assertEqual(foo.name, "")
