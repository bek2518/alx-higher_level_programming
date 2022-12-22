#!/usr/bin/python3
'''
Prints the state Object with name passed as an argument
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

    name = sys.argv[4]
    instance = session().query(State).filter(State.name.like(name)).all()
    if instance:
        print("{}".format(instance[0].id))
    else:
        print("Not Found")

    session().close()
