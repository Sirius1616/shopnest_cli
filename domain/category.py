#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class BaseRepository:
    """Base repository responsible for database operations"""

    def __init__(self, db_url="sqlite:///shopnest.db"):
        """Initialize database engine and session"""
        self.engine = create_engine(db_url)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def new(self, obj):
        """Add object to session"""
        self.session.add(obj)

    def save(self):
        """Commit changes"""
        self.session.commit()

    def delete(self, obj=None):
        """Delete object from session"""
        if obj:
            self.session.delete(obj)

    def all(self, model):
        """Return all objects of a model"""
        return self.session.query(model).all()