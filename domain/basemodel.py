#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """Class that is the base and every other class inherits from"""
    def __init__(self):
        """Init method to instantiate the classes"""

        self.id = str(uuid.uuid())
        created_at = datetime.now()
        updated_at = datetime.now()


    def __str__(self):
        """A string representation of how the class will be strown when the string method is called on the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"




