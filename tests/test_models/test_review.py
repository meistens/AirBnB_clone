#!/usr/bin/python3
"""Modules needed for place class test"""
import unittest
import pycodestyle
from models.review import Review


class Review_test(unittest.TestCase):
    """test class for review class"""
    def test_doc(self):
        """checks if documentation exists for review"""
        docs = Review.__init__.__doc__
        self.assertGreater(len(docs), 1)

    def test_str_format(self):
        """Tests the __str__ is correct"""
        strFormat = Review()
        str_format = "[Review] ({}) {}".format(strFormat.id,
                                               strFormat.__dict__)
        self.assertEqual(str_format, str(strFormat))

    def test_dict(self):
        """Tests to_dict"""
        dicts = Review()
        to_dict = dicts.to_dict()
        self.assertEqual(type(to_dict), dict)
        for attr in dicts.__dict__:
            self.assertTrue(attr in to_dict)

    def test_place(self):
        """Tests if review just works"""
        foo = Review()
        self.assertEqual(type(foo).__name__, "Review")

    def test_name_attr(self):
        """Tests if review instance has a text attribute, and it is empty"""
        foo = Review()
        self.assertTrue(hasattr(foo, "text"))
        self.assertEqual(foo.text, "")

    def test_id_attr(self):
        """Test if review has a place_id attr, and is empty"""
        foo = Review()
        self.assertTrue(hasattr(foo, "place_id"))
        self.assertEqual(foo.place_id, "")

    def test_user_id_attr(self):
        """Test if review has a user_id, and it is empty"""
        foo = Review()
        self.assertTrue(hasattr(foo, "user_id"))
        self.assertEqual(foo.user_id, "")
