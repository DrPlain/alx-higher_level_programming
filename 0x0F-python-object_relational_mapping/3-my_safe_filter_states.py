#!/usr/bin/python3
"""lists all states where name mathces arg passed from db hbtn_0e_0_usa

    Usage: ./3-my_safe_filter_states.py <mysql username> \
                                <mysql passwd> \
                                <database name> \
                                <state name searched>
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s \
            ORDER BY states.id", (argv[4],))
    states = cursor.fetchall()
    [print(state) for state in states if state[1] == argv[4]]
    cursor.close()
    db.close()
