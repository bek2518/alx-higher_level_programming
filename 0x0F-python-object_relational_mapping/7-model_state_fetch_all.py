#!/usr/bin/python3
'''
Lists all state objects from the database
'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    for instance in session().query(State).order_by(State.id).all():
        print("{}: {}".format(instance.id, instance.name))
    session().close()
