#!/usr/bin/python3
"""Modules needed for place class test"""
import unittest
import pycodestyle
from models.place import Place


class City_test(unittest.TestCase):
    """test class for city class"""
    def test_doc(self):
        """checks if documentation exists for city"""
        docs = Place.__init__.__doc__
        self.assertGreater(len(docs), 1)

    def test_str_format(self):
        """Tests the __str__ is correct"""
        strFormat = Place()
        str_format = "[Place] ({}) {}".format(strFormat.id,
                                              strFormat.__dict__)
        self.assertEqual(str_format, str(strFormat))

    def test_dict(self):
        """Tests to_dict"""
        dicts = Place()
        to_dict = dicts.to_dict()
        self.assertEqual(type(to_dict), dict)
        for attr in dicts.__dict__:
            self.assertTrue(attr in to_dict)

    def test_place(self):
        """Tests if place just works"""
        foo = Place()
        self.assertEqual(type(foo).__name__, "Place")

    def test_name_attr(self):
        """Tests if place instance has a name attribute, and it is empty"""
        foo = Place()
        self.assertTrue(hasattr(foo, "name"))
        self.assertEqual(foo.name, "")

    def test_id_attr(self):
        """Test if place has a city_id attr, and is empty"""
        foo = Place()
        self.assertTrue(hasattr(foo, "city_id"))
        self.assertEqual(foo.city_id, "")

    def test_user_id_attr(self):
        """Test if place has a user_id, and it is empty"""
        foo = Place()
        self.assertTrue(hasattr(foo, "user_id"))
        self.assertEqual(foo.user_id, "")

    def test_descr_attr(self):
        """Test if place has a description attribute, and is empty"""
        foo = Place()
        self.assertTrue(hasattr(foo, "description"))
        self.assertEqual(foo.description, "")

    def test_number_rooms_attr(self):
        """ Test if place has attribute number_rooms, and is 0 """
        foo = Place()
        self.assertTrue(hasattr(foo, "number_rooms"))
        self.assertEqual(foo.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """ Test if place has attribute number_bathrooms, and is 0 """
        foo = Place()
        self.assertTrue(hasattr(foo, "number_bathrooms"))
        self.assertEqual(foo.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """Test if place has attribute max_guest, and is 0 """
        foo = Place()
        self.assertTrue(hasattr(foo, "max_guest"))
        self.assertEqual(foo.max_guest, 0)

    def test_price_by_night_attr(self):
        """ Test if place instance has attribute price_by_night, and is 0 """
        foo = Place()
        self.assertTrue(hasattr(foo, "price_by_night"))
        self.assertEqual(foo.price_by_night, 0)

    def test_latitude_attr(self):
        """Test if place instance has attribute latitude, and is 0.0 """
        foo = Place()
        self.assertTrue(hasattr(foo, "latitude"))
        self.assertEqual(foo.latitude, 0.0)

    def test_longitude_attr(self):
        """ Test if place instance has attribute longitude, and is 0.0 """
        foo = Place()
        self.assertTrue(hasattr(foo, "longitude"))
        self.assertEqual(foo.longitude, 0.0)

    def test_amenity_ids_attr(self):
        """ Test if place instance has attribute amenity_ids, and is empty """
        foo = Place()
        self.assertTrue(hasattr(foo, "amenity_ids"))
        self.assertEqual(foo.amenity_ids, [])
