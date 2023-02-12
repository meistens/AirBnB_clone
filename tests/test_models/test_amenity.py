#!/usr/bin/python3
"""Modules for testing amenity class"""
import unittest
import pycodestyle
from models.amenity import Amenity

class Amenity_test(unittest.TestCase):
    """test class for amenity class"""
    def test_doc(self):
        """checks if documentation exists for amenity"""
        docs = Amenity.__init__.__doc__
        self.assertGreater(len(docs), 1)

    def test_str_format(self):
        """Tests the __str__ is correct"""
        strFormat = Amenity()
        str_format = "[Amenity] ({}) {}".format(strFormat.id,
                                                strFormat.__dict__)
        self.assertEqual(str_format, str(strFormat))

    def test_dict(self):
        """Tests to_dict"""
        dicts = Amenity()
        to_dict = dicts.to_dict()
        self.assertEqual(type(to_dict), dict)
        for attr in dicts.__dict__:
            self.assertTrue(attr in to_dict)

    def test_amenity(self):
        """Tests if amenity just works"""
        foo = Amenity()
        self.assertEqual(type(foo).__name__, "Amenity")

    def test_name_attr(self):
        """Tests if it has attributes, and it is empty"""
        foo = Amenity()
        self.assertTrue(hasattr(foo, "name"))
        self.assertEqual(foo.name, "")
