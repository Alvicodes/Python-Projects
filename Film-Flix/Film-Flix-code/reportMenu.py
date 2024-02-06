import readFilms

def read_report():
    try:
        with open("filmReports.txt") as reportRead:
            rr = reportRead.read()
        return rr
    
    except FileNotFoundError as nf:
        print(f"Check {nf}")

def search_film():
        option = 0
        optionLists = ["1","2","3","4","5"]
        
        reportMenu = read_report()        
        while option not in optionLists:
            print(reportMenu)
            option = input("Enter a number from the list provided. ")
        return option
        

def reports():
    filmProgram = True
    while filmProgram: #While True
        film_menu = search_film()
        
        match film_menu:
            case "1":
                readFilms.read_films()
            case "2":
                readFilms.film_genre()
            case "3":
                readFilms.film_year()
            case "4":
                readFilms.film_rating()
            case _:
                filmProgram = False   
    input("Press the 'Enter' key to Exit: ")
    
if __name__ == "__main__":
    reports()