#!/usr/bin/python3

from domain.base_model import BaseModel


class Product(BaseModel):
    """Class defines the product to be purchased or ordered by a User"""
    def __init__(self, name: str, price: float, *args, **kwargs):
        super().__init__(*args, **kwargs)
