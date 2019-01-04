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

print(MinNum)
print(MaxNum)
print(SecretNum)