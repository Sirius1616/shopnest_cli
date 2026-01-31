#!/usr/bin/python3
from domain.base_model import BaseModel

class Order(BaseModel):
    """Model defining the orders made from different Users on a particular product"""
    def __init__(self, user_id = None, product_ids = None, total = None, *args, **kwargs):
        """Instantiating the order class but with an inheritance of the init method of the basemodel class"""
        super().__init__(*args, **kwargs)
        
        if user_id != None:
            self.user_id = user_id
        if product_ids != None:
            self.product_ids = product_id
        if total != None:
            self.total = total
