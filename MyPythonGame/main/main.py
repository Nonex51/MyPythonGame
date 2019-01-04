#MyPythonGame Project For RSG

from random import *
def PlayAgain(play):
    again=str(input("Do you want to play again, type yes or no "))
    print(again)
    try:
       val = str(again)
       print (val)
    except ValueError:
        print("That's not response!")
        print("Write Yes or Y or yes or y")
    print (val)

    if again == "yes" or again =="YES" or again =="y" or again =="Y":         
       main()
    if again == "no":                     #don'twant to enter in this loop 
       play = False
    return play


def Intro():
    print("Hello, my name is Eve")
    print("What is your name ?")
    user_name = input()
    print("Hello "+ user_name)
    MaxRange = 20
    MinNum= randint(0, MaxRange)
    MaxNum = randint(99 + MinNum, 100 + MaxRange )
    SecretNum = randint(MinNum, MaxNum )

    print("I am thinking of a number between "+ str(MinNum) + " and " + str(MaxNum) + ", care to take a guess?")
    return SecretNum


def Game(SecretNum):
    play = True
    while play:
        NumTry = 0
        MaxTry = 5

        for NumTry in range(0,MaxTry):
            UserNum = input()  
            try:
                val = int(UserNum)
            except ValueError:
                 print("That's not an number!")
                 print("No.. input string is not a int number. It's a string")
             
            if UserNum == SecretNum:
                print("You guessed correctly!")
                break
            else:
               print("You guessed wrong, sorry!")
               NumTry += 1
        print("    ")
        print("You had try " + str(NumTry) + " times")
        PlayAgain(play)
        break

                     
def main():
    Game(Intro())
    

main()

