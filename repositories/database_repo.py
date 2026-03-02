#!/usr/bin/python3



class DBStorage:
    """Database storage class where the data is stored on the mysql"""

    __engine = None
    __session = None

    def __init__(self):
