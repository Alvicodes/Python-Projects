from connect import *

def delete_film():
    
    try:
        idField = input("Enter the ID of the Film you want to delete: ")
        myCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {idField}")
        row = myCursor.fetchone()
        
        if not row:
            print(f"Film ID {idField} does not exist in the database.")
        else:
            myCursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField}")
            myDB.commit()
            print(f"Film with ID {idField} has successfully been deleted.")
    
    except sql.OperationalError as e:
        myDB.rollback()
        print(f"No information found: {e}")

if __name__ == "__main__":
    delete_film()

