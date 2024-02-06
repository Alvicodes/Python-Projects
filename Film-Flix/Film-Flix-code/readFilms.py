from connect import *

def read_films():
    try:
        rows = myCursor.execute(f"SELECT * FROM tblFilms").fetchall()

        if not rows:
            print("No record(s) exists")
        else:
            for aFilm in rows:
                print(aFilm)
            
    except sql.OperationalError as e:
        print(f"Records not found: as {e}")
if __name__ == "__main__":
    read_films()


def film_genre():
    try:
        valid_genres = ["Horror","Fantasy","Action","Crime","Animation","Fighting","Comedy"]
        
        while True:
            idField = input("Enter the Genre you would like to search from the following\nHorror / Fantasy / Action / Crime / Animation / Fighting / Comedy:\n")
            if idField in valid_genres:
                break
            else:
                print(f"No film with Genre {idField} exists")
            
        myCursor.execute(f" SELECT * FROM tblFilms WHERE genre = '{idField}'")
        
        rows = myCursor.fetchall()
        
        if not rows:
            print(f"No film with Genre {idField} exists")
        else:
            for aRecord in rows:
                print(aRecord)  
    except sql.OperationalError as e:
            myDB.rollback()
            print(f"Genre does not exist in the Database: {e}")      
if __name__ == "__main__":   
    film_genre()
              
def film_year():
    while True:
        try:
            idField = input("Enter the Release Year you would like to search:\n")
            myCursor.execute(f" SELECT * FROM tblFilms WHERE yearReleased = '{idField}'")
            rows = myCursor.fetchall()
            
            if not rows :
                print(f"No film on record was released in {idField}")
            else:
                for aRecord in rows:
                    print(aRecord)
                break  
        except sql.OperationalError as e:
            myDB.rollback()
            print(f"Please check {e} and try again")
if __name__ == "__main__":   
    film_year()
        
def film_rating():
    try:
        valid_ratings = ["PG","G","R"]
        
        while True:
            idField = input("Enter the Rating you would like to search from the following\nPG / G / R:\n")
            if idField in valid_ratings:
                break
            else:    
                print(f"Invalid search criteria!")
        
        myCursor.execute(f" SELECT * FROM tblFilms WHERE rating = '{idField}'")
        rows = myCursor.fetchall()
        
        if not rows:
            print(f"No film with rating {idField} exists")
        else:
            for aRecord in rows:
                print(f"Films with rating {idField}:")
                print(aRecord)  
    except sql.OperationalError as e:
        myDB.rollback()
        print(f"Rating does not exist in the Database: {e}")
if __name__ == "__main__":   
    film_rating()
        
