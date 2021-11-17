#!/usr/bin/python3
"""Display cities"""
import MySQLdb
import sys


def list_cities():
    """Takes arguments argv to list from database
    Only lists with states that matches name argument
    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    if len(sys.argv) == 5:
        conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM\
    cities INNER JOIN states ON cities.state_id = states.id;")

    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    list_cities()
