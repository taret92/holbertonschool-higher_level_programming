#!/usr/bin/python3
"""script that prints the first state from
the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    """main function"""
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, passwd, db))

    Base.metadata.create_all(engine)
    session = Session(engine)

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
