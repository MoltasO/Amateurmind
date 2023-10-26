'''
Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6.
Du ska försöka gissa denna kods siffor på max tolv drag.
Efter respektive gissning så kommer du att få en respons:
För varje gissad korrekt siffra på korrekt plats i koden: ✔
För varje gissad korrekt siffra på fel plats i koden: ☐
För de siffor som inte finns med i koden ges ingen markering.
Exempel: om den slumpade koden är 2315
och du gissar 3165
så blir responsen "✔☐ ✔"
Du får välja mellan två svårighetsnivåer:
Lättare nivå: Alla siffor är garanterat olika
Svårare nivå: Det kan finnas upprepningar av en eller flera siffror
'''

import random
running = True
debug = True

settings = {
    "number of guesses": 10,
    "right number right place": "✔",
    "right number wrong place": "☐",
    "wrong number wrong place": " ",
}
#
#███████████████████████
#█                     █
#█ 1   1 2 3 4   ✔✔✔✔  █
#█ 2   1 2 3 4   ✔✔✔✔  █
#█ 3   1 2 3 4   ✔✔✔✔  █
#█ 4   1 2 3 4   ✔✔✔✔  █
#█ 5   1 2 3 4   ✔✔✔✔  █
#█ 6   1 2 3 4   ✔✔✔✔  █
#█ 7   1 2 3 4   ✔✔✔✔  █
#█ 8   1 2 3 4   ✔✔✔✔  █
#█ 9   1 2 3 4   ✔✔✔✔  █
#█ 10  1 2 3 4   ✔✔✔✔  █
#█                     █
#█ Gissningar kvar: 8  █
#███████████████████████
#

#settings["right number right place"]

def input_(texts: str):
    return input(f"{texts} -> ")    

def gissning() -> list[int]:
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
        while len(list_) < 4:
            num_to_add = random.randint(1,6)
            if num_to_add not in list_:
                list_.append(num_to_add)
    elif diff == 2:
        while len(list_) < 4:
            list_.append(random.randint(1,6))
    if debug:
        print(list_)
    return list_  
          
def draw(answer_list: list[str], feedback: list[str]):
    #middle_part = ""
    for i in range(0, settings["number of guesses"]):
        middle_part = ""
        middle_part += f"█{i+1: <4}{answer_list[0]}   {feedback[0]}  █"
        print(middle_part)
#gameboard = f"""
#██████████████████████████
#█       Mastermind       █
#█                        █
#█ 1                      █
#█ 2   1 2 3 4   ✔ ✔ ✔ ✔  █
#█ 3   1 2 3 4   ✔ ✔ ✔ ✔  █
#█ 4   1 2 3 4   ✔ ✔ ✔ ✔  █
#█ 5   1 2 3 4   ✔ ✔ ✔ ✔  █
#█ 6   1 2 3 4   ✔ ✔ ✔ ✔  █
#█ 7   1 2 3 4   ✔ ✔ ✔ ✔  █
#█ 8   1 2 3 4   ✔ ✔ ✔ ✔  █
#█ 9   1 2 3 4   ✔ ✔ ✔ ✔  █
#█ 10  1 2 3 4   ✔ ✔ ✔ ✔  █
#█                        █
#█   Gissningar kvar: 8   █
#██████████████████████████
#"""
    #print(gameboard)

def game(diff: int):
    """
    Main loop for the game.
    """
    feedback_list = []
    guess_list = []
    answer = createnums(diff) # Creates the code you're trying to guess.
    for i in range(1,settings["number of guesses"]): #Guess loop
        user_guess = gissning()
        guess_list.append(" ".join(str(e) for e in user_guess))
        if debug:
            print(user_guess, answer)
        feedback_str = ""
        for i in range(0,len(user_guess)):
            if answer[i] == user_guess[i]:
                feedback_str += settings["right number right place"]
            elif user_guess[i] in answer:
                feedback_str += settings["right number wrong place"]
            else:
                feedback_str += settings["wrong number wrong place"]
        print(feedback_str)
        feedback_list.append(" ".join(feedback_str))
        draw(guess_list, feedback_list)


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