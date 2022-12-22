#!/usr/bin/python3
'''
Adds the state Louisiana to the database
'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)

    instance = session.query(State).filter(State.id.like(2)).first()
    instance.name = "New Mexico"
    session.commit()
    session.close()
