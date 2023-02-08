#!/usr/bin/env python3

# modules needed for the test case

import unittest
from datetime import datetime
from models.base_model import BaseModel
import json

class BaseModel_test(unittest.TestCase):
    # test class for the BaseModel class
    def test_doc(self):
         # checks documentation exists
        docs = BaseModel.__init__.__doc__
        self.assertTrue()

    def test_datetime(self):
        # compares the created_at and updated_at dates (should not be the same)
       created_at_date = BaseModel()
       updated_at_date = BaseModel()
       self.assertNotEqual(created_at_date.created_at, updated_at_date.updated_at)
       self.assertNotEqual(updated_at_date.created_at, created_at_date.updated_at)
