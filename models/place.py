#!/usr/bin/python3

from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity


class Place(BaseModel):
    '''The Place class'''
    city_id = ''
    City.id = city_id
    user_id = ''
    User.id = user_id
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    Amenity.id = amenity_ids
