#!/usr/bin/python3
""" State Module for HBNB project """
from __future__ import annotations
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    storage_type = getenv("HBNB_TYPE_STORAGE", "fs")
    if storage_type == 'db':
        cities = relationship('City', back_populates='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            from models import storage
            city_class = models.City
            city_instances = storage.all(city_class)
            return [city for city in city_instances.values() if city.state_id == self.id]

from models.city import City
