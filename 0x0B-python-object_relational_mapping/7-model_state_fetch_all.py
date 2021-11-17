#!/usr/bin/python3
"""lists all State objects from the database SQLalchemy method"""
import sys
import sqlalchemy
from sqlalchemy import (create_engine)
from sqlalchemy.engine.base import Engine
from model_state import Base, State
from sqlalchemy.orm import query_expression, session, sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    s = session()
    for state in s.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    s.close
