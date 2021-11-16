#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa that start with N"""


import MySQLdb
import sys


def state_N(argv):
    """Takes arguments argv to list from database
    Only lists with states that start with N
    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()

    cur.execute("SELECT * FROM states\
                WHERE state.name LIKE 'N%'\
                ORDER BY state.id ASC")

    for row in cur.fetchall():
        print("{}".format(row))
    cur.close()
    conn.close()

    if __name__ == "__main__":
        state_N()