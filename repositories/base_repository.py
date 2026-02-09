#!/usr/bin/python3
import os
import json


class BaseRepository:
    """The storage engine that create way for the serialization of the classes"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""

        return self.__objects


    def new(self, obj):
        """Sets in __object the obj with key <obj class name>.id"""
        key = f'{obj.__class__.__name__}.{obj.id}'

        self.__objects[key] = obj

        return self.__objects

    
    def save(self):
        """Serialize all the objects and save to JSON file"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as f:
                json.dump(obj_dict, f)


    def reload(self):
        """The method that deserialized the json objects back to python objects"""

       
        from domain.user import User
        from domain.order import Order
        from domain.product import Product
        from domain.base_model import BaseModel
        

        classes = {'BaseModel': BaseModel, 'User': User, 'Product': Product, 'Order': Order}


        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                des_obj = json.load(f)

            for key, value in des_obj.items():

                class_name = value.get("__class__")

                if class_name in classes:
                    cls = classes[class_name]
                    self.__objects[key] = cls(**value)
                else:
                    print("Class name don't exist")
                    continue

        else:
            pass






