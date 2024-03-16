# Object-relational mapping

For application code to communicate with a relational database engine, we need a driver than can directly interact with the DB, execuing queries as passed.  
MySQLdb is an interface to the popular MySQL database server that provides the Python database API.

An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into objects used in application code. It provides a high-level abstraction allowing one to just use application code without writing SQL queries. ORMs rely on the drivers to interact with the **relational** DB and then **map** the result to an **object**.

Python has ORMs like [SQLAlchemy](https://www.sqlalchemy.org/), [Django ORM](https://docs.djangoproject.com/en/dev/topics/db/), etc.  
For this project we use **SQLAlchemy** (_version 1.4.52_).
