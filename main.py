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
debug = False


#Settings that affect the game
settings = {
    "number of guesses": 10,
    "right number right place": "✔",
    "right number wrong place": "☐",
    "wrong number wrong place": " ",
    "background_character": " ",
    "win_message": "\n"+"#"*10+" DU VANN!!!! "+"#"*10+"\n",
    "fail_message": "\nDu förlorade :("
}

def input_(texts: str):
    return input(f"{texts} -> ")    

def gissning() -> list[int]:
    """
    A input checker that filters out and numbers.
    """
    listan_gissning= []
    while True:
        kod_gissning= (input_("\nAnge gissning som föjld av fyra siffror"))
        if not (len(kod_gissning) == 4):
            print("Ogilitig gissning, måste inehålla fyra siffror.\n")
        elif not kod_gissning.isdigit():
            print("Ogilitig gissning, får endast inehålla nummer.\n")
        elif (int(kod_gissning) < 1111) or (int(kod_gissning) > 6666):
            print("Ogilitig gissning, får endast inehålla nummer 1 till 6.\n")
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
    where as the 2nd setting allows duplicates.
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
          
def draw(answer_list: list[str], feedback: list[str], guesses: int):
    """
    Draws a custom handmade "gui" in the
    terminal takes 2 list arguments and a int.
    """

    top_part = """\

    
██████████████████████████
█       Mastermind       █
█                        █
"""

    bottom_part = """\
█                        █
█{}█
██████████████████████████
"""


    middle_part = "" #Draws the correct amount of "Segments" depending on the game settings.
    for i in range(0, settings["number of guesses"]):
        try:  #Checks if the index exists in the lists.
            middle_part += f"█ {i+1: <4}{answer_list[i]}   {feedback[i]}  █\n"      #Used Guess Segment
        except IndexError:
            middle_part += f"█ {i+1: <4}{settings['background_character']*19}█\n"   #Unused Guess Segment
    bottom_text = f"{str(guesses)+' Gissningar kvar': ^24}"
    print(top_part+middle_part+bottom_part.format(bottom_text)) # Display in terminal

def game(diff: int):
    """
    Main loop for the game.
    """
    feedback_list = [] #List of str contains the feedback.
    guess_list = []  #List of int contains user guesses.
    answer = createnums(diff) # Creates the code you're trying to guess.
    for guess_num in range(1,settings["number of guesses"]+1): #Guess loop
        user_guess = gissning()
        guess_list.append(" ".join(str(e) for e in user_guess))
        if debug:
            print(user_guess, answer)
        feedback_str = ""
        for char in range(0,len(user_guess)): #Goes thrugh the answer and checks what is right.
            if answer[char] == user_guess[char]:
                feedback_str += settings["right number right place"]
            elif user_guess[char] in answer:
                feedback_str += settings["right number wrong place"]
            else:
                feedback_str += settings["wrong number wrong place"]
        feedback_list.append(" ".join(feedback_str))
        draw(guess_list, feedback_list, settings['number of guesses']-guess_num) #Draws gui
        if user_guess == answer: # Does some special thing if you win
            print(settings["win_message"]) 
            break
        elif guess_num == settings["number of guesses"]:
            print(settings["fail_message"])
            break
        else:
            pass
            #draw(guess_list, feedback_list, settings['number of guesses']-guess_num) #Draws gui
def main():
    """
    Function used to as "init" for the game loop function.
    """
    while running:
        dif_inp = str(input_("Vilken svårighetsgrad vill du spela på? e (Enkel) / s (Svår)"))
        if dif_inp.isalpha():
            if  dif_inp.lower() == "e":
                game(diff=1)
                break
            elif dif_inp.lower() == "s":
                game(diff=2)
                break
        else:
            print(f"{dif_inp} är inte en accepterad input.\n")
    


if __name__ == "__main__":
    main()