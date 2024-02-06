from connect import *

def update_film():
    idField = input("Enter the ID of the Film you want to update: ")
    fieldName = input("Enter the name of the value to be updated:\n(title / yearReleased / rating / duration / genre ):\n ")
    fieldValue = input("Enter the new value: ")
    fieldValue = "'"+fieldValue+"'"
    
    try:
        myCursor.execute(f"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE filmID = {idField}")
        myDB.commit()
        print(f"The {fieldName} of film with ID {idField} has been updated")
        
    except sql.OperationalError as e:
        print(f"Update failed: {e}")
        
if __name__ == "__main__":
    update_film()

