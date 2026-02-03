#!/usr/bin/python3
from domain.base_model import BaseModel


class BaseRepository:
    """The storage engine that create way for the serialization of the classes"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""

        return BaseRepository.__objects


    def new(self, obj):
        """Sets in __object the obj with key <obj class name>.id"""
        key = f'{self.__class__.__name__}.{self.id}'

        BaseRepository.__objects[key] = obj

        return BaseRepository.__objects


