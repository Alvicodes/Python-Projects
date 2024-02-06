import addFilm, deleteFilm, updateFilm, readFilms, reportMenu


def read_file():
    try:
        with open("menuOption.txt") as fileRead:
            fr = fileRead.read()
        return fr  
    except FileNotFoundError as nf:
        print(f"Check {nf}")


def films_menu():
    fOption = 0
    fOptionList = ["1","2","3","4","5","6"]
    
    menuChoices = read_file()
    
    while fOption not in fOptionList:
        print(menuChoices)
        
        fOption = input("Enter a number from the list provided. ")
        
        if fOption not in fOptionList:
            print(f"{fOption} is not a valid choice!")
    return fOption

mainProgram = True
while mainProgram: #While True
    mainMenu = films_menu()#
    
    match mainMenu:
        case "1":
            addFilm.insert_film()
        case "2":
            deleteFilm.delete_film()
        case "3":
            updateFilm.update_film()
        case "4":
            readFilms.read_films()
        case "5":
            reportMenu.reports()
        case _:
            mainProgram = False 
input("Press the 'Enter' key to exit the program: ")   
