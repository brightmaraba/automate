import sys
from random import randint

randomInteger = randint(0, 20)

while True:
    print("I have guessed a number between 0 and 20, what do you think it is?")
    userGuess = int(input())
    if userGuess  < randomInteger:
        print("My guess is much higher, try again?")
    elif userGuess > randomInteger:
        print("My guess is lower, try again?")
    else:
        break

print("Yep, you got it.")
