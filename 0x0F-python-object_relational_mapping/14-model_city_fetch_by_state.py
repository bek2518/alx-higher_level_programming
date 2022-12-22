#!/usr/bin/python3
'''
Prints all cities from database
'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)

    for state, city in session.query(State, City).\
            filter(State.id == City.state_id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
