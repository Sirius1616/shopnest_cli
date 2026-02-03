#!/usr/bin/python3
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
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            for key in self.__objects.to_dict():
                json.dump(key, f)



