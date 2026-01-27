#!/usr/bin/python3
from domain.base_model import BaseModel

class Order(BaseModel):
    """Model defining the orders made from different Users on a particular product"""
    def __init__(self, *args, **kwargs):
        """Instantiating the order class but with an inheritance of the init method of the basemodel class"""
        super().__init__(*args, **kwargs)

        self.user_id = user_id
        self.product_ids = product_id
        self.total = total
