#!/usr/bin/python3
""" Class that defines a DB storage engine """
import os
from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import sessionmaker
USER = os.environ.HBNB_MYSQL_USER
PSWD = os.environ.HBNB_MYSQL_PWD
HOST = os.environ.HBNB_MYSQL_HOST
DTBS = os.environ.HBNB_MYSQL_DB
ENV = os.environ.HBNB_ENV


class DBStorage():
    """ Class method """
    __engine = None
    __session = None

    def __init__(self):
        """ Creating the engine and the session """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            USER, PSWD, HOST, DTBS), pool_pre_ping=True)
        if ENV == 'test':
            m = MetaData()
            m.reflect(self.__engine)
            m.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query the current DB and return all objects """
        if cls is None:
            query = "SELECT * FROM *"
        else:
            query = select(cls)
        result = self.__session.execute(query).all()
        print(result)
        for row in result:
            print(row)

    def reload(self):
        """ Create all tables in th current DB and the current session """
        Session = sessionmaker(self.__engine)
        self.__session = Session()

    def new(self, obj):
        """ Adding an object to the current DB """
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """ Committing all changes of the current DB """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an instance from the current DB """
        if obj is not None:
            self.__session.delete(obj)
            self.save()
