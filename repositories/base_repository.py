#!/usr/bin/python3
import os
import json
from domain.base_model import BaseModel


class BaseRepository:
    """The storage engine that create way for the serialization of the classes"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""

        return self.__objects


    def new(self, obj):
        """Sets in __object the obj with key <obj class name>.id"""
        key = f'{self.__class__.__name__}.{self.id}'

        self.__objects[key] = obj

        return self.__objects

    
    def save(self):
        """Serialize all the objects and save to JSON file"""
        obj_dict = {}
        for key, value in self.__objects.to_dict().items():
            obj_dict[key] = value

        with open(self.__file_path, 'w', encoding='utf-8') as f:
                json.dump(obj_dict, f)


    def reload(self):
        """The method that deserialized the json objects back to python objects"""

        if os.path.exist(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                des_obj = json.load(f)
            return des_obj
        else:
            pass






