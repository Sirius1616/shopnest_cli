#!/usr/bin/python3
import json


class FileStorage:
    """Handles JSON file persistence"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all stored objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Add new object"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize objects to JSON"""
        obj_dict = {}

        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def delete(self, obj=None):
        """Delete object"""
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]