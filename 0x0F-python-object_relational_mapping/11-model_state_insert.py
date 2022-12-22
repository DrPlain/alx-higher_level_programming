#!/usr/bin/python3
""" Adds the State obj 'Louisiana' to the db hbtn_0e_6_usa
Usage: ./10-model_state_my_get.py <mysql username>\
                                    <mysql passwd>\
                                    <database name>
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(id=6, name='Louisiana')
    session.add(new_state)
    session.commit()

    session.flush()
    print(new_state.id)
