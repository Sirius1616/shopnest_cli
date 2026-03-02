#!/usr/bin/python3
from sqlalchemy import create_engine



class DBStorage:
    """Database storage class where the data is stored on the mysql"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiates the engines created"""
        self.__engine = create_engine("mysql+pymysql://root:password@localhost/mydatabase")
