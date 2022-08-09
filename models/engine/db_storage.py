#!/usr/bin/python3
"""  """
import os
from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import Session
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
        with Session(self.__engine) as session:
            query = select()
            result = session.execute(query).all()
            for row in result:
                print(row[0])
