#!/usr/bin/python3

import json
from os import path

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    'BaseModel' : BaseModel,
    'User' : User,
    'Place' : Place,
    'State' : State,
    'City' : City,
    'Amenity' : Amenity,
    'Review' : Review
}


class FileStorage:
    '''FileStorage class which serialized and deserializes files'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Return the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''Create a new FileStorage object'''
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj
        return self.__objects

    def save(self):
        '''Save the FileStorage object to JSON file'''
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            temp = {}
            temp.update(self.__objects)
            for key, value in temp.items():
                temp[key] = value.to_dict()
            json.dump(temp, f)

    def reload(self):
        '''Reload the FileStorage object from JSON file'''

        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key,val in temp.items():
                    self.__objects[key] = classes[val['__class__']](**val)
