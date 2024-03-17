#!/usr/bin/python3
"""
This script  takes in the name of a state
as an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """
  db_connect = db.connect()
  Cur = db_connect.cursor()
  if ';' in argv[4]:
    pass
  else:
    Cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name LIKE '%{}' ORDER BY citites.id".format(argv[4]))
    result = Cur.fetchall()
    for row in result:
        x = ",".join(row)
        print(f"{x}, ", end = "")
      
