#!/usr/bin/python3
"""Modules needed for city class test"""
import unittest
import pycodestyle
from models.city import City

class City_test(unittest.TestCase):
    """test class for city class"""
    def test_doc(self):
        """checks if documentation exists for city"""
        docs = City.__init__.__doc__
        self.assertGreater(len(docs), 1)

    def test_str_format(self):
        """Tests the __str__ is correct"""
        strFormat = City()
        str_format = "[City] ({}) {}".format(strFormat.id,
                                                strFormat.__dict__)
        self.assertEqual(str_format, str(strFormat))

    def test_dict(self):
        """Tests to_dict"""
        dicts = City()
        to_dict = dicts.to_dict()
        self.assertEqual(type(to_dict), dict)
        for attr in dicts.__dict__:
            self.assertTrue(attr in to_dict)

    def test_amenity(self):
        """Tests if amenity just works"""
        foo = City()
        self.assertEqual(type(foo).__name__, "City")

    def test_name_attr(self):
        """Tests if it has attributes, and it is empty"""
        foo = City()
        self.assertTrue(hasattr(foo, "name"))
        self.assertEqual(foo.name, "")
