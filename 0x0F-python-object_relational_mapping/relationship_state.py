#!/usr/bin/python3
""" This module create Class Base.
See:
    ./6-model_state.py test file
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


""" Declarative: system to define classes mapped to relational database tables
"""
Base = declarative_base()


class State(Base):
    """
    class State that inherits from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")
