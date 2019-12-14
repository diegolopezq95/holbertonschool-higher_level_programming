#!/usr/bin/python3
""" This module adds the State object "California” and
the City “San Francisco” from the database hbtn_0e_100_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
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
    """Insert a new State object to database
    """
    add_state = State(name="California")
    add_city = City(name="San Francisco")
    add_city.state = add_state
    session.add(add_state)
    session.add(add_city)
    session.commit()
    """query() takes one or more entities and returns a
    new Query object which will issue mapper queries within
    the context of this Session
    """
    session.close()
