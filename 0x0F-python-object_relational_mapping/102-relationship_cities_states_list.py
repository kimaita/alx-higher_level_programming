#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_101_usa"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    with Session(engine) as session:
        stmt = select(City).order_by('id')

        for city in session.scalars(stmt):
            print(f"{city.id}: {city.name} -> {city.state.name}")
