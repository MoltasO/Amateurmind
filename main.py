import random

difficulties = ["Easy","Hard"] # game(dif=1), game(dif=2)
running = True
debug = True

settings = {
    "number of guesses": 10
}

def input_(texts: str):
    return input(f"{texts} -> ")    

def gissning():
    """
    A input checker that filters out and numbers.
    """
    listan_gissning= []
    while True:
        kod_gissning= (input_("Ange gissning som föjld av fyra siffror"))
        if not (len(kod_gissning) == 4):
            print("Ogilitig gissning, m")
        elif not kod_gissning.isdigit():
            print("Ogilitig gissning, får endast inehålla nummer.")
        else:
            for char in kod_gissning:
                char=int(char)
                listan_gissning.append(char)
            return listan_gissning
            
def createnums(diff:int) -> list[int]:
    """
    Create a list of numbers to 
    be the code you're trying to guess
    has two settings using 1 and 2
    where the first setting creates a list
    of random numbers that does not have any duplicates
    whereas the 2nd setting allows it.
    """
    list_ = []
    if  diff == 1:
        for i in range(1,5):
            if i not in(list_):
                list_.append(random.randint(1,6))
    elif diff == 2:
        for i in range(1,5):
            list_.append(random.randint(1,6))
    if debug:
        print(list_)
    return list_  
          
def draw():
    '''
    Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6.
    Du ska försöka gissa denna kods siffor på max tolv drag.
    Efter respektive gissning så kommer du att få en respons:
    För varje gissad korrekt siffra på korrekt plats i koden: ✔
    För varje gissad korrekt siffra på fel plats i koden: ☐
    För de siffor som inte finns med i koden ges ingen markering.
    Exempel: om den slumpade koden är 2315
    och du gissar 3165
    så blir responsen ✔☐☐
    Du får välja mellan två svårighetsnivåer:
    Lättare nivå: Alla siffor är garanterat olika
    Svårare nivå: Det kan finnas upprepningar av en eller flera siffror
    '''
    pass


def game(diff: int):
    """
    Main loop for the game.
    """
    user_answers = []
    answer = createnums(diff) # Creates the code you're trying to guess.
    for i in range(1,settings["number of guesses"]): #Guess loop
        user_guess = gissning()
        ""
        #draw()
        for i in user_guess:
            if i in answer and user_guess.index(i) in answer.index(i):
                pass
            elif i in answer:
                pass
            else:
                pass

def main():
    while running:
        dif_inp = str(input_("What difficulty do you want to play on? e (Easy), h (Hard)"))
        if dif_inp.isalpha():
            if  dif_inp.lower() == "e":
                game(diff=1)
                break
            elif dif_inp.lower() == "h":
                game(diff=2)
                break
        else:
            print("Invalid input, try again. \n")
    


if __name__ == "__main__":
    main()