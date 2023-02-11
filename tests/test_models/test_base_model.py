#!/usr/bin/python3
"""Defines the modules used for testing"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
import json
import pycodestyle

class BaseModel_test(unittest.TestCase):
    """test class for the BaseModel class"""
    def test_doc(self):
        """checks if documentation exists (should be a docstring, not # ...)"""
        docs = BaseModel.__init__.__doc__
        self.assertGreater(len(docs), 1)

    def test_datetime(self):
        """compares the created_at and updated_at dates (should not be the same)"""
        created_at_date = BaseModel()
        updated_at_date = BaseModel()
        self.assertNotEqual(created_at_date.created_at, updated_at_date.updated_at)
        self.assertNotEqual(updated_at_date.created_at, created_at_date.updated_at)

    def test_str_format(self):
        """Tests if the __str__is correct (it should be)"""
        strFormat = BaseModel()
        str_format = "[BaseModel] ({}) {}".format(strFormat.id, strFormat.__dict__)
        self.assertEqual(str_format, str(strFormat))

    def test_uuid(self):
        """Tests if UUID is unique (it should be!)"""
        uuid_1 = BaseModel()
        uuid_2 = BaseModel()
        self.assertNotEqual(uuid_1.id, uuid_2.id)

    def test_dict(self):
        """Tests if dict is a dictionary """
        serial = BaseModel()
        self.assertTrue(dict, type(serial.to_dict()))

    def test_keys(self):
        """Tests if to_dict has the right keys"""
        keys = BaseModel()
        self.assertIn("id", keys.to_dict())
        self.assertIn("__class__", keys.to_dict())
        self.assertIn("created_at", keys.to_dict())
        self.assertIn("updated_at", keys.to_dict())

    def test_attrs(self):
        """Tests if to_dict has the right attributes"""
        attr = BaseModel()
        attr.name = "foo"
        attr.number = 3
        self.assertIn("name", attr.to_dict())
        self.assertIn("number", attr.to_dict())

    def test_kwargs(self):
        """Test kwargs arttributes (the script won't cut it)"""
        kwargs = BaseModel()
        kwargs.name = "foo"
        kwargs.number = 3
        jsonModel = kwargs.to_dict()
        kwargs2 = BaseModel(**jsonModel)
        self.assertTrue(isinstance(kwargs2, BaseModel))
        self.assertTrue(isinstance(jsonModel, dict))
        self.assertTrue(kwargs is not kwargs2)

    def test_pycodestyle(self):
        """Test if code conforms to pycodestyle"""
        pycode = pycodestyle.StyleGuide()
        results = pycode.check_files(["models/base_model.py"])
        self.assertEqual(results.total_errors, 0)
