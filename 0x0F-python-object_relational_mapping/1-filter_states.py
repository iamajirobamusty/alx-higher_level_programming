

#!/usr/bin/python3
"""
This script retrieve all the states from the database `hbtn_0e_0_usa`
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_connect = MySQLdb.connect(host='localhost', prot=3306, user=argv[1], password=argv[2], db=argv[3])
    Cur = db_connect.cursor()
    Cur.execute("SELECT * FORM states WHERE name LIKE BINARY 'N%' ORDER BY states.id")
    result = Cur.fetchall()
    for col in result:
        print(col)
    Cur.close()
    db_connect.close()
