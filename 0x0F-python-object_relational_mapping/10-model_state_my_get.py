#!/usr/bin/python3
"""States object module"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    state = sys.argv[4]
    session = Session()
    instance = session.query(State).\
        order_by(State.id).filter(State.name == state).first()
    if instance is not None:
        print("{}".format(instance.id))
    else:
        print("Not found")
    session.close()
