#!/usr/bin/python3
""" This module prints the State object with the name passed as argument
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    state_name = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    """Session object provides the entrypoint to acquire a Query object
    """
    Session = sessionmaker(bind=engine)

    session = Session()
    """query() takes one or more entities and returns a
    new Query object which will issue mapper queries within
    the context of this Session
    """
    state = session.query(State).filter(State.name == str(state_name))
    if state.count() != 1:
        print("Not found")
    else:
        print("{}".format(state[0].id))
    session.close()
