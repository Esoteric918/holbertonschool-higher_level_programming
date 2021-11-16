#!/usr/bin/python3

import sys
import MySQLdb

def safe_states():
     """Takes arguments argv to list from database
    Only lists with states that matches name argument
    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: state name
    """
if len(sys.argv) == 5:
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                       passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s\
                ORDER BY id ASC",(sys.argv[4],))

    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    safe_states()