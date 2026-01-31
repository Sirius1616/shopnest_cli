#!/usr/bin/python3

from domain.base_model import BaseModel


class Product(BaseModel):
    """Class defines a product to be purchased or ordered by a User"""
    
    def __init__(self, name=None, price=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Type checks if values are provided
        if name is not None and not isinstance(name, str):
            raise TypeError(f"name must be a string, got {type(name).__name__}")
        
        if price is not None and not isinstance(price, float):
            raise TypeError(f"price must be a float, got {type(price).__name__}")
        
        # Assign attributes
        self.name = name
        self.price = price

