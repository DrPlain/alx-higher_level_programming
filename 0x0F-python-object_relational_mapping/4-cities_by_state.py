#!/usr/bin/python3
"""lists all cities from the db hbtn_0e_4_usa
    Usage: ./4-cities_by_sate.py <mysql username> \
                                <mysql passwd> \
                                <database name>
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
    cursor.execute("SELECT cities.id, cities.name, states.name\
            FROM cities INNER JOIN states\
            ON cities.state_id = states.id\
            ORDER BY cities.id")

    cities = cursor.fetchall()
    [print(city) for city in cities]
    cursor.close()
    db.close()
