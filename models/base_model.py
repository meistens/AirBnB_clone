#!/usr/bin/python3
"""Defines the BaseModel class"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """This class defines the behaviours of all properties/methods and attributes for other classes"""

    def __init__(self):
        """Public instance attributes for initializing a new BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """Returns/prints the string of the object instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attributes"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all key/value pairs of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
