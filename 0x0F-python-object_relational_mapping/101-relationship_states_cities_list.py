#!/usr/bin/python3
'''
Lists all state objects and corresponding city object
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)

    state_list = session.query(State).all()
    for states in state_list:
        print("{}: {}".format(states.id, states.name))
        for cities in states.cities:
            print("\t{}: {}".format(cities.id, cities.name))
    session.close()
