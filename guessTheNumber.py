#This is a random number game
import random
secretNumber = random.randint(1, 100)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess the 6 times
for guessesTaken in range(1,7):
    print('Take a guess: ')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print(f'Good Job! You guessed it in {guessesTaken} guesses')
else:
    print(f'Nope. The number I was thinking of was {secretNumber}')