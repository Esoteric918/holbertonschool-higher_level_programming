#!/usr/bin/python3
""" takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=argv[1],
                           passwd=argv[2], db=argv[3], port=3306)

    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states WHERE BINARY name = '{}'\
                ORDER BY .id ASC".format(argv[4]))

    thing = cur.fetchall()
    for row in thing:
        print(row)

    cur.close()
    conn.close()
