#!/usr/bin/python3

from repositories.engine.file_storage import FileStorage


class BaseRepository:
    """Repository layer that interacts with storage"""

    def __init__(self):
        self.storage = FileStorage()

    def all(self):
        """Return all objects"""
        return self.storage.all()

    def new(self, obj):
        """Add new object"""
        self.storage.new(obj)

    def save(self):
        """Save objects"""
        self.storage.save()

    def delete(self, obj=None):
        """Delete object"""
        self.storage.delete(obj)