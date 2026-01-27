#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """Class that is the base and every other class inherits from"""
    def __init__(self, *args, **kwargs):
        """Init method to instantiate the classes"""
        
        if kwargs:
            for key, value in kwargs.items():
                self.id = str(uuid.uuid4())
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def __str__(self):
        """A string representation of how the class will be strown when the string method is called on the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__})"


    def save(self):
        "Saves an update of any model created"
        self.updated_at = datetime.now()


    def to_dict(self):
        "Returns the dictionary representation of the class"
        dictn = {}

        dictn['__class__'] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dictn[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
            else:
                dictn[key] = value

        return dictn




