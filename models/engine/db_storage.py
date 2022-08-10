#!/usr/bin/python3
""" Class that defines a DB storage engine """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
USER = os.environ.get('HBNB_MYSQL_USER')
PSWD = os.environ.get('HBNB_MYSQL_PWD')
HOST = os.environ.get('HBNB_MYSQL_HOST')
DTBS = os.environ.get('HBNB_MYSQL_DB')
ENV = os.environ.get('HBNB_ENV')


class DBStorage():
    """ Class method """
    __engine = None
    __session = None

    classes = {
        'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def __init__(self):
        """ Creating the engine and the session """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            USER, PSWD, HOST, DTBS), pool_pre_ping=True)
        if ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query the current DB and return all objects """
        values = dict()
        if cls is None:
            # for cls in self.classes.values():
            # result = self.__session.query(cls)
            query = self.__session.query(State)
        else:
            query = self.__session.query(DBStorage.classes[cls])
        result = self.__session.execute(query).all()
        return {f"{type(k).__name__}.{k.id}": k
                for k in [row[0] for row in result]}

    def reload(self):
        """ Create all tables in th current DB and the current session """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
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
