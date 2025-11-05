#!/usr/bin/python3
""" db storage module"""
from __future__ import annotations
import os
from models.state import State
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.city import City


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ.get('HBNB_MYSQL_USER'),
            os.environ.get('HBNB_MYSQL_PWD'),
            os.environ.get('HBNB_MYSQL_HOST'),
            os.environ.get('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        """Query objects from the database based on class name."""
        all_objects = {}
        classes = [State, City]  # Add other models to this list

        if cls:
            classes = [cls]

        for class_ in classes:
            query_result = self.__session.query(class_).all()
            for obj in query_result:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                all_objects[key] = obj

        return all_objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine, expire_on_commit=False))

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
