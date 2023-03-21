#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    '''amenity class'''
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
=======
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""
>>>>>>> cbaedfdd56b6e339a0af634cae7c81972e647043
