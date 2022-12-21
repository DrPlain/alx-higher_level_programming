#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa
    Usage: ./0-select_states.py <mysql username> <mysql passwd> <database name>
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
    cursor.execute('SELECT * FROM states ORDER BY states.id')
    states = cursor.fetchall()
    [print(state) for state in states]
