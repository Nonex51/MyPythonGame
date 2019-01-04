#MyPythonGame Project For RSG

from random import *

print("Hello, my name is Eve")
print("What is your name ?")
user_name = input()
print("Hello "+ user_name)

range = 20
MinNum= randint(0, range)
MaxNum = randint(99 + MinNum, 100 + range )
SecretNum = randint(MinNum, MaxNum )

#""" DEBUG
print(MinNum)
print(MaxNum)
print(SecretNum)
#"""

print("I am thinking of a number between "+ str(MinNum) + " and " + str(MaxNum) + ", care to take a guess?")
UserNum = int(input())

print(UserNum)

if UserNum == SecretNum:
    print("You guessed correctly!")
else:
    print("You guessed wrong, sorry!")