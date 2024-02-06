from connect import *

def insert_film():
    films = []
    filmTitle = input("Enter Film Title: ")
    filmReleaseDate = input("Enter Film Release Date: ")
    filmRating = input("Enter Film Rating: ")
    filmDuration = input("Enter Film Duration: ")
    filmGenre = input("Enter Film Genre: ")
    
    films.append([filmTitle, filmReleaseDate, filmRating, filmDuration, filmGenre])
    
    
    try:
       myCursor.execute("INSERT INTO tblFilms VALUES(NULL, ?, ?, ?, ?, ?)", tuple(films[0]))
       myDB.commit()
       print(f"{filmTitle} has been inserted into the Table.")
    except sql.OperationalError as e:
        myDB.rollback()
        print(f"Attempt to insert {filmTitle} has failed. {e}")
if __name__ == "__main__":
    insert_film()
    