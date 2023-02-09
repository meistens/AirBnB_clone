#!/usr/bin/python3
"""Initialize modules"""
from models.base_model import BaseModel
import json

class FileStorage():
    """A private class for the serialization and deserialization class of objects to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """Sets an object in the __objects dictionary with a key of <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes the __objects to the JSON file"""
        emp_dict = {}
        for key, value in self.__objects.items():
            emp_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(emp_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
                for key, value in self.__objects.items():
                    class_name = value["__class__"]
                    obj = eval(class_name + "(**value)")
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
