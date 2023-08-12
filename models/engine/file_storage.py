#!/usr/bin/python3

"""
    File Storage Module
"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
        File Storage - serializes and deserializes to JSON file

            Attributes:
                __file_path: location of the file
                __objects: dictionary to store object ids
            Methods:
                all: returns the dictionary __objects
                new: sets in __object the id
                save: serializes the __objects to json
                reload: deserializes the json
    """
    __file_path = "{}/{}".format(os.path.abspath(os.getcwd()), "file.json")
    print(__file_path)
    __objects = {}

    def all(self):
        """ Returns a dict of objects """
        return self.__objects

    def new(self, obj):
        """ Sets an obj to the __object"""
        name = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[name] = obj

    def save(self):
        """ Serializes the objects to json"""
        serialized_objects = {key: value.to_dict()
                              for key, value in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """ Deserialization of the json"""
        try:
            with open(self.__file_path) as f:
                des_data = json.load(f)
                for key, value in des_data.items():
                    cls_name = value['__class__']
                    self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            pass
