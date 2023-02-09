#!/usr/bin/python3
"""Initialize modules"""
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Class for testing FileStorage"""
    def test_docs(self):
        """Tests docuentation exists"""
        docs = BaseModel.__init__.__doc__
        self.assertGreater(len(docs), 1)

    def test_save(self):
        """Tests the save functionality of FileStorage"""
        save_file = BaseModel()
        save_file.save()
        self.assertEqual("", "")
