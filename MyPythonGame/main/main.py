#MyPythonGame Project For RSG

from random import *

def CompareValidGuess(SecretNum,val,win):
     if val == SecretNum:
        print("You guessed correctly!")
        win = True
        print(win)
        return win
     if val < SecretNum:
        print("It's more")
        return 
     if val > SecretNum :
        print("It's less")
        return 
     else:
        print("You guessed wrong, sorry!")          #EXIT
        return    

def PlayAgain(play):
    again=str(input("Do you want to play again, put yes or no "))
    try:
       val = str(again)  
    except ValueError:
        print("That's not response!")
        print("Write Yes or Y or yes or y")
    if again == "yes" or again =="YES" or again =="y" or again =="Y":         
       InGame()
    if again == "no":                    
       play = False
    return play

def Intro():
    print("Hello, my name is Eve")
    print("What is your name ?")
    user_name = input()
    print("Hello "+ user_name)
    return user_name

def RandomSecretNum():
    MaxRange = 20
    MinNum= randint(0, MaxRange)
    MaxNum = randint(99 + MinNum, 100 + MaxRange )
    SecretNum = randint(MinNum, MaxNum )
    print("I am thinking of a number between "+ str(MinNum) + " and " + str(MaxNum) + ", care to take a guess?")
    return SecretNum

def Game(SecretNum):
    play = True
    win = False
    while play:
        NumTry = 0
        MaxTry = 10
        for NumTry in range(0,MaxTry):
            UserNum = input()  
            try:
                val = int(UserNum)
            except ValueError:
                 print("That's not an number!")
                 print("No.. input string is not a int number. It's a string")
            NumTry += 1
            if  CompareValidGuess(SecretNum,val,win) == True:
                PlayAgain(play)
                return
            else:
                print("You had try " + str(NumTry) + " times")
        print("You haven't sucess to guessed the number, Try again!")       #EXIT
        return    

  
def InGame():                
    Game(RandomSecretNum())

def main():
    Intro()
    InGame()
    
main()

