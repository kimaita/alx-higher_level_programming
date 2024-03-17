#!/usr/bin/python3
""" lists the first State object from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    with Session(engine) as session:
        stmt = select(State).order_by('id').limit(1)
        try:
            s = session.scalars(stmt).one_or_none()
            print(f"{s.id}: {s.name}")
        except Exception as e:
            print('Nothing')
