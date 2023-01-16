#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    '''The Base Class'''
    id = f'{uuid.uuid4()}'
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        '''Print instance details'''
        return (f'[{__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        '''Updates the time of update'''
        updated_at = datetime.now()
        return updated_at

    def to_dict(self):
        '''Returns dictionary containing all keys/values of __dict__'''
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__
        self.id = self.id
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return obj_dict
