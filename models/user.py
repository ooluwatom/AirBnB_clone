#!/usr/bin/python3

from base_model import BaseModel

class User(BaseModel):
    '''The User class'''
    def __init__(self):
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
