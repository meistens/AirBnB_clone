#!/usr/bin/env python3

# initializing modules
import uuid
import models
from datetime import datetime

class BaseModel:
    # Class that defines the behaviours of all properties/methods and
    # attributes for other classes

    def __init__(self):
        # Public instance attributes
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        # Returns/prints the string of the object
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    # Public instance methods
    def save(self):
        # updates the public instance attributes
        self.updated_at = datetime.now()

    def to_dict(self):
        # returns a dictionary containing all key/value pairs of __dict__ of the instance
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict.update({"created_at": self.created_at.isoformat()})
        new_dict.update({"updated_at": self.updated_at.isoformat()})
        return new_dict
