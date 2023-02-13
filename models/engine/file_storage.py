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
import os


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
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    # def save(self):
    #     """Serializes the __objects to the JSON file"""
    #     emp_dict = {}

    #     for key, value in self.__objects.items():
    #         emp_dict[key] = value.to_dict()
    #     with open(self.__file_path, "w") as f:
    #         json.dump(emp_dict, f)

    def save(self):
        """Serializes the __objects to the JSON file"""
<<<<<<< HEAD
=======
        emp_dict = {}
        
        for key, value in self.__objects.items():
            emp_dict[key] = value.to_dict()
>>>>>>> 4e39f04d9d28446dd97a3f468d3b863dfac4423d
        with open(self.__file_path, "w") as f:
            json.dump({
                k: value.to_dict() for key,
                value in self.__objects.items()}, f)

    # def reload(self):
    #     """Deserializes the JSON file to __objects"""
    #     try:
    #         with open(self.__file_path, "r") as f:
    #             self.__objects = json.load(f)
    #             for key, value in self.__objects.items():
    #                 class_name = value["__class__"]
    #                 obj = eval(class_name + "(**value)")
    #                 self.__objects[key] = obj
    #     except FileNotFoundError:
    #         pass

    def reload(self):
        """Deserializes the JSON file to __objects"""
        current_classes = {"BaseModel", "User", "Amenity", "City", "State",
                           "Place", "Review"}
        with open(self.__file_path, "r") as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return

            self.__objects = {key: current_classes[key.split('.')[0]](**value)
                              for key, value in deserialized.items()}
    # def delete(self, obj=None):
    #     if obj:
    #         key = "{}.{}".format(obj.__class__.__name__, obj.id)
    #         if key in self.__objects:
    #             del self.__objects[key]
