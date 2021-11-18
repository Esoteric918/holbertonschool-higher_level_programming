#!/usr/bin/python3
"""lists all State objects from the database SQLalchemy method"""
import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from model_state import Base, State
from sqlalchemy.orm import query_expression, session, sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    S = sessionmaker(bind=engine)
    try:
        print("{}: {}".format(S().query(State).first().id,
                              S().query(State).first().name))
    except Exception:
        print('Nothing')
