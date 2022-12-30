#!/usr/bin/python3
"""
Creates the State California with the city San Francisco
from the db hbtn_0e_100_usa
Usage: ./14-model_city_fetch_by_state.py <mysql username>\
                                         <mysql passwd>\
                                         <database name>

"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State
from sys import argv

user = argv[1]
passwd = argv[2]
db = argv[3]

if __name__ == "__main__":
    # create database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, passwd, db))

    # create a transaction session
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
