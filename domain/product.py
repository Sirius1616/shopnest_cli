#!/usr/bin/python3

from domain.base_model import BaseModel


class Product(BaseModel):
    """Class defines the product to be purchased or ordered by a User"""
    def __init__(self, name = None, price = None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not isinstance(name, str):
            raise TypeError(f"name must be a string, got {type(name).__name__}")
        if not isinstance(price, float):
            raise TypeError(f"price must be a float, got {type(price).__name__}")

        self.name = name
        self.price = price

