#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
#
# Imports
#
import os
from random import randint
from art import logo
from art import ASCIIGameOver
from art import ASCIIWinner
#
# Global variables
#
HARD_MODE = 5
EASY_MODE = 10

#
# Private functions
#

# clearConsole
def clearConsole():
    """
    Clears console.
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# setDifficulty
def setDifficulty():
    # Difficulty
    difficulty = input("Choose the 'hard' or the 'easy' way: ").lower()
    # Hard mode on!
    if difficulty == 'hard':
        # oh oh 
        return HARD_MODE
    elif difficulty == 'easy':
        return EASY_MODE
    else:
        print("Wrong choice!")
        return 0

# GuessDaNumba
def GuessDaNumba():
    # print logo
    print(logo)
    # Generate random number
    correctAnswer = randint(1, 100)
    # Turns
    turns = setDifficulty()
    # Play
    guess = -1
    while turns != 0 and guess != correctAnswer:
        print(f"You have only {turns} turns left... choose wisely!")
        guess = int(input("Your guess: "))
        # guess == correctAnswer
        if guess == correctAnswer:
            print(ASCIIWinner)
            return
        elif guess < correctAnswer:
            print("Too low...")
            turns -= 1
        elif guess > correctAnswer:
            print("Too big...")
            turns -= 1 
    # Game Over
    print(ASCIIGameOver)
    return 
        





#
# main
#
if __name__ == "__main__":
    clearConsole()
    GuessDaNumba()