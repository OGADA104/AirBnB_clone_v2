#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), nullable=False)
    user_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column((1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
