#!/usr/bin/python3
"""Display cities"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities, states\
                WHERE states.id = state_id\
                ORDER BY id ASC")

    thing = cur.fetchall()
    for row in thing:
        print(row)

    cur.close()
    conn.close()
