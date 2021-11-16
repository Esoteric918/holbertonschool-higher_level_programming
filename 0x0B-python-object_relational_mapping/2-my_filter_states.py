#!/usr/bin/python3
""" takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
"""


import sys
import MySQLdb


def main():
    """func - main - args"""
    if len(sys.agrv) != 5:
        print("Enter 4 arguments")
        return
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE state.name ='{}'\
                .format(agrv[4]) ORDER BY state.id ASC")

    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

    if __name__ == "__main__":
        main(sys.argv)
