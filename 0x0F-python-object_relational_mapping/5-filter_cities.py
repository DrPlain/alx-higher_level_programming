#!/usr/bin/python3
"""Takes a state name as arg and lists all cities
of the state from the db hbtn_0e_4_usa
Usage: ./5-filter_cities.py <mysql username> \
                            <mysql passwd> \
                            <database name> \
                            <state name>
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
    cursor.execute("SELECT cities.name FROM cities INNER JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id", (argv[4],))

    cities = cursor.fetchall()
    for idx, city in enumerate(cities):
        if idx <= len(cities) - 2:
            print(city[0], end=', ')
        else:
            print(city[0], end='')
    print("")
    cursor.close()
    db.close()
