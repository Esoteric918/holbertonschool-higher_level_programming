#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

def main(agrv):
    """func - main - args"""
    if len(agrv) != 4:
        print("Enter 3 arguments")
        return
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=agrv[1],
        passwd=agrv[2],
        db=agrv[3],
        charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall()
        print(row)
    conn.close()

    if __name__ == "__main__":
    import sys
    main(sys.argv)
