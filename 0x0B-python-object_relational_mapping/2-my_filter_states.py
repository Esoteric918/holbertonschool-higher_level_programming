#!/usr/bin/python3
""" takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY state.name ='{}'"
                "ORDER BY state.id ASC".format(sys.agrv[4]))

    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
