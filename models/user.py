#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    '''The User class'''
    def __init__(self):
        User.email = ''
        User.password = ''
        User.first_name = ''
        User.last_name = ''
