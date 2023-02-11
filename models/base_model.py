#!/usr/bin/python3
"""Defines the BaseModel class"""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel():
    """This class defines the behaviours of all properties/methods and attributes for other classes"""
    def __init__(self, *args, **kwargs):
        """Public instance attributes for initializing a new BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:    
            models.storage.new(self)
                
    def __str__(self):
        """Returns/prints the string of the object instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attributes"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all key/value pairs of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
