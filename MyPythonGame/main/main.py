#MyPythonGame Project For RSG

import sys
from sys import exit
from random import *

print("Hello, my name is Eve")
print("What is your name ?")
user_name = input()
print("Hello "+ user_name)

MaxRange = 20
MinNum= randint(0, MaxRange)
MaxNum = randint(99 + MinNum, 100 + MaxRange )
SecretNum = randint(MinNum, MaxNum )

""" DEBUG
print(MinNum)
print(MaxNum)
print(SecretNum)
"""

print("I am thinking of a number between "+ str(MinNum) + " and " + str(MaxNum) + ", care to take a guess?")


NumTry = 0
MaxTry = 10

for NumTry in range(0,MaxTry):
    UserNum = input()
    if UserNum == SecretNum:
        print("You guessed correctly!")
    else:
        print("You guessed wrong, sorry!")
    NumTry += 1
print()  
print("You had try " + str(NumTry) + " times")  

#sys.exit()   
#quit()
#raise SystemExit
#exit()