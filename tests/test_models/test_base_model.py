#!/usr/bin/python3
"""Defines the modules used for testing"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
import json

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

