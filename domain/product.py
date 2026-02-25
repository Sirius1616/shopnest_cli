#!/usr/bin/python3

from domain.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey


class Product(BaseModel):
    """Class defines a product to be purchased or ordered by a User"""

    __tablename__ = 'products'
    
    name = Column(String(128), nullable=False)
    category_id = Column(String(60), ForeignKey('category.id'), nullable=False)

