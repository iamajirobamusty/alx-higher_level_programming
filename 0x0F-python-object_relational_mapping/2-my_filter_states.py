
#!/usr/bin/python3
"""
This script retrieve all the states from the database `hbtn_0e_0_usa`
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_connect = MySQLdb.connect(host='localhost', prot=3306, user=argv[1], password=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()
    db_cusor.execute("SELECT * FORM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(argv[4]))
    result = db_cursor.fetchall()
    for col in result:
        print(col)
    db_cursor.close()
    db_connect.close()
