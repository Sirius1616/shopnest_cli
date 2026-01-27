#!/usr/bin/python3

from domain.base_model import BaseModel


class User(BaseModel):
    """User modoel that inherits from the BaseModel that defines the users"""
    def __init__(self, name = None, email = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.email = email

