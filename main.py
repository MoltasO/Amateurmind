import random
difficulties = ["Easy","Hard"] # game(dif=1), game(dif=2)
running = True
#def gissning():
#    while True:
#        kod_gissning= str(input("Ange gissning som föjld av fyra siffror"))
#        if kod_gissning.isdigit:
#            for char in kod_gissning:

def input_(texts: str):
    return input(f"{texts} -> ")

def draw():
    pass

def game(diff: int):
    pass

def main():
    while running:
        dif_inp = str(input_("What difficulty do you want to play on? e (Easy), h (Hard)"))
        if dif_inp.isalpha() and dif_inp.lower() == "e":
            game(diff=1)
            break
        elif dif_inp.isalpha() and dif_inp.lower() == "h":
            game(diff=2)
            break
        else:
            print("Invalid input, try again. \n")
    
        

if __name__ == "__main__":
    main()