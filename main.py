import random
difficulties = ["Easy","Hard"]

#def gissning():
#    while True:
#        kod_gissning= str(input("Ange gissning som föjld av fyra siffror"))
#        if kod_gissning.isdigit:
#            for char in kod_gissning:

def input_(texts: str):
    return input(f"{texts} -> ")


def main():
    while True:
        dif_inp = str(input_("What difficulty do you want to play on?"))
        if dif_inp.isalpha():
            print("Text")
        else:
            print("Invalid input, try again. \n")
            

if __name__ == "__main__":
    main()