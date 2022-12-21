#!/usr/bin/python3
"""lists all states with a name starting with N(upper N) from db hbtn_0e_0_usa
    Usage: ./0-select_states.py <mysql username> \
                                <mysql passwd> \
                                <database name> \
                                <state name searched>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' \
            ORDER BY states.id".format(sys.argv[4]))
    states = cursor.fetchall()
    [print(state) for state in states if state[1] == sys.argv[4]]
    cursor.close()
    db.close()
