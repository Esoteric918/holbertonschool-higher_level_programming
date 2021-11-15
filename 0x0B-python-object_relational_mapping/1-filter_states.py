#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

from sys import argv
import MySQLdb


def main(argv):
    """func - main - args"""
    if len(argv) != 4:
        print("Enter 3 arguments")
        return
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name='N%' ORDER BY state.id ASC")


    for row in cur.fetchall():
        print("{}".format(row))
    cur.close()
    conn.close()

    if __name__ == "__main__":
        import sys
    main(sys.argv)
