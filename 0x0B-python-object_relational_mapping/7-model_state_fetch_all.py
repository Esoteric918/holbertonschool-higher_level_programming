#!/usr/bin/python3

import sys
import sqlalchemy
from sqlalchemy import (create_engine)
from sqlalchemy.engine.base import Engine
from model_state import Base, State
from sqlalchemy.orm import query_expression, session, sessionmaker

if __name__ == "__main__":

    Session = sessionmaker(Engine)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(sys.argv[1], sys.argv[2],
                        sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    s = session()
    for state in s.query(State).order_by(state.id).all():
        print("{}: {}".format(state.id, state.name))
    s.close
