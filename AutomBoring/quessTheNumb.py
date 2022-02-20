#This is a guess the number game.
import random

print('Hello. What is your name.')
name = input()

print('Well, ' + name + ' I am thinking a number between 1 to 20.')
secretNum = random. randint(1, 20)

for guessesTaken in range (1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNum:
        print('Your guess it too low.')
    elif guess > secretNum:
        print('Your guess is too high.')
    else:
        break   #This is for correct test.

if guess == secretNum:
    print('Good job ' + name + '. You guessed the my number in ' + str(guessesTaken) + ' guess.')
else:
    print('Nope. The number I was thinking of was ' + str(secretNum))

print('You took ' + str(guessesTaken) + ' guesses.')