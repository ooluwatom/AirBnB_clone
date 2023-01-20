#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    '''The Base Class'''
    def __init__(self, *args, **kwargs):
        '''Base model __init__ method'''
        if kwargs:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''Print instance details'''
        return (f'[{__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        '''Updates the time of update'''
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Returns dictionary containing all keys/values of __dict__'''
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
