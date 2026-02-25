#!/usr/bin/env python3

from domain.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String


class Category(BaseModel):
    """Category class that shows the grouping of Items inheriting attributes from Basemodel"""

    __tablename__ = 'categories'

    name = Column(String(128), nullable=False)

