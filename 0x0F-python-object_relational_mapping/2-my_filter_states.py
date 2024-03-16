#!/usr/bin/python3
"""displays all states in the database hbtn_0e_0_usa where
 name matches a given argument.
"""
import MySQLdb
import sys


def connect_db(user, pwd, db_name):
    """Creates and returns a connection to the `db_name` database as `user`

    Args:
        user (str): User to connect to the database as
        pwd (str): User password
        db_name (str): Name of database to connect to

    Returns:
        Connection
    """
    return MySQLdb.connect(user=user, password=pwd,
                           database=db_name)


def query_db(conn, state):
    """Returns the result of an SQL query over the Connection `conn`

    Args:
        conn (Connection): MySQLdb Connection to use

    Returns:
        tuple(tuple)
    """
    c = conn.cursor()
    sql_query = """
    SELECT *
    FROM states
    WHERE name = "{0}"
    ORDER BY id"""
    c.execute(sql_query.format(state))
    return c.fetchall()


def execute_task(args):
    """Lists states from the database hbtn_0e_0_usa with names matching
      the given name

    Args:
        args (list[str]): list of MySQL connection arguments:
                [mysql_username, mysql_password, database_name, state_name]
    """
    if len(args) >= 3:
        conn = connect_db(args[0], args[1], args[2])
        result = query_db(conn, args[3])
        for city in result:
            print(city)


if __name__ == "__main__":
    args = sys.argv[1:]
    execute_task(args)
