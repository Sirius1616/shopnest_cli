#!/usr/bin/env python3
import os
from domain.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String


class Category(BaseModel):
    """Category class that shows the grouping of Items inheriting attributes from Basemodel"""

    __tablename__ = 'categories'

    name = Column(String(128), nullable=False)
    category_id = Column(String(60), primary_key=True, nullable=False)

    if os.getenv('')


