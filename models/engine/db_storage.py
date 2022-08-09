#!/usr/bin/python3
"""  """
import os
from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import sessionmaker
USER = os.environ.HBNB_MYSQL_USER
PSWD = os.environ.HBNB_MYSQL_PWD
HOST = os.environ.HBNB_MYSQL_HOST
DTBS = os.environ.HBNB_MYSQL_DB
ENV = os.environ.HBNB_ENV


class DBStorage():
    """ """
    __engine = None
    __sessions = None

    def __init__(self):
        """ """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            USER, PSWD, HOST, DTBS), pool_pre_ping=True)
        if ENV == 'test':
            m = MetaData()
            m.reflect(self.__engine)
            m.drop_all(self.__engine)

    def all(self, cls=None):
        if cls is None:
            query = "SELECT * FROM *"
        else:
            query = select(cls)
        result = self.__sessions.execute(query).all()
        print(result)
        for row in result:
            print(row)

    def reload(self):
        Session = sessionmaker(self.__engine)
        self.__sessions = Session()
