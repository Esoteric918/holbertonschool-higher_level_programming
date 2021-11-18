#!/usr/bin/python3
#!/usr/bin/python3
"""lists first State object from the database SQLalchemy method"""
from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from model_state import Base, State
from sqlalchemy.orm import query_expression, session, sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    S = Session()
    try:
        print(S.query(State).filter(State.name == argv[4]).first(),"{}".format(id))
    except Exception:
        print ("Not found")
    S.close



