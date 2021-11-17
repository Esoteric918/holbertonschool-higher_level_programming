#!/usr/bin/python3
""" takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
"""
from sys import argv
import MySQLdb


def state_N():
    """Take arguments argv to list from database -
    gets states that start with N
    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    conn = MySQLdb.connect(host="localhost", user=argv[1],
                           passwd=argv[2], db=argv[3], port=3306)

    cur = conn.cursor()
    cur.execute("SELECT is, name FROM states WHERE BINARY name = '{}'\
                ORDER BY .id ASC".format(argv[4]))

    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    state_N
