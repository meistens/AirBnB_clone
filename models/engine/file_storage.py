#!/usr/bin/python3
"""Initialize modules"""
from models.base_model import BaseModel
import json
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """A private class for the serialization and deserialization class of
    objects to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """Sets an object in the __objects dictionary with
        a key of <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes the __objects to the JSON file"""
        obj_dict = {obj: self.__objects[obj].to_dict() for
                    obj in self.__objects.keys()}
        with open(self.__file_path) as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for value in obj_dict.values():
                    class_name = value["__class__"]
                    del class_name
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            return
