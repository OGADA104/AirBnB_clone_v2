#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from collections import OrderedDict


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = OrderedDict()

    def delete(self, obj=None):
        """delete object"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del self.__objects[key]
        else:
            pass

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            key = "{}".format(cls.__name__)
            return {obj_key: obj for obj_key,
                    obj in self.__objects.items() if obj_key.startswith(key)}
        else:
            return list(self.__objects.values())

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        return self.__objects

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        if self.__file_path:
            try:
                with open(self.__file_path, 'r') as file:
                    objects_dict = json.load(file)
                    for key, obj_dict in objects_dict.items():
                        class_name, obj_id = key.split('.')
                        obj_class = classes.get(class_name)
                        if obj_class:
                            obj_instance = obj_class(**obj_dict)
                            self.__objects[key] = obj_instance
            except FileNotFoundError:
                pass
        else:
            pass
