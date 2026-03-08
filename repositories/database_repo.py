#!/usr/bin/python3
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine



load_dotenv()
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')

class DBStorage:
    """Database storage class where the data is stored on the mysql"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiates the engines created"""
        self.__engine = create_engine("mysql+pymysql://root:password@localhost/mydatabase", pool_pre_ping=True)

    def all(self, cls=None):
        """query on the database session all objects depending on the class name"""
        session = self.__engine(ping=True)
        self.__session = session()
        self.__session.query_all()
        
