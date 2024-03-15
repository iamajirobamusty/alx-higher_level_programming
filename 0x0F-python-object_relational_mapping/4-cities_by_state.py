#!/usr/bin/python3

"""
Script to print out all the cities from the  database htbn_0e_4_usa
"""
import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    db_connection = db.connect(host='localhost', port=3306, user=argv[1], password=argv[2], db=argv[3])
    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT cities.id, cities.name, states.name FROM JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"%(argv[4]))
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print("row")
