#!/usr/bin/python3
""" This module deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
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
    for state in session.query(State).filter(State.name.like("%a%")):
        session.delete(state)
    session.commit()
    session.close()
