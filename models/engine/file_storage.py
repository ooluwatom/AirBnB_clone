#!/usr/bin/python3

import json
from os import path


class FileStorage:
    '''FileStorage class which serialized and deserializes files'''
    def __init__(self):
        self.__file_path = 'objects.json'
        self.__objects = {}

    def all(self):
        '''Return the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''Create a new FileStorage object'''
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj
        return self.__objects

    def save(self):
        '''Save the FileStorage object to JSON file'''
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        '''Reload the FileStorage object from JSON file'''
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                json_dict = json.loads(f.read())
                for k, v in json_dict.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
        else:
            pass
