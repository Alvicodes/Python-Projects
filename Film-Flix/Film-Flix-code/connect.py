import sqlite3 as sql

try:
    with sql.connect("filmflix.db") as myDB:
        myCursor =myDB.cursor()
        
except sql.OperationalError as e:
    print(f"Connection to Database failed: {e}")