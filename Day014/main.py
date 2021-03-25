


#
# Imports
#
import os
import random
from art import logo
from art import vs
from game_data import data

#
# Global variables
#


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

# getRandomAccount
def getRandomAccount():
    """
    Returns a random account from game_data.py.-
    """
    randomNumber = random.choice(data)
    return randomNumber

# AccountInfo
def AccountInfo(account):
    """
    Prints formatted account data.-
    """
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# printAvsB
def printAvsB(accountA, accountB):
    print(AccountInfo(accountA))
    print(vs)
    print(AccountInfo(accountB))

# checkFollowers
def checkFollowers(guess, aCount, bCount):
    if aCount > bCount:
        answer = 'a'
    else:
        answer = 'b'
    return (answer == guess)

# GreaterOrLowerThanGame
def GreaterOrLowerThanGame():
    """
    Insert description.-
    """
    # Print logo
    print(logo)
    # Define user score
    userScore = 0
    # Define shouldContinue
    shouldContinue = True
    # Get two random accounts
    accountA = getRandomAccount()
    accountB = getRandomAccount()

    # Play
    while shouldContinue:
        # Update B and A
        accountB = accountA
        accountA = getRandomAccount()
        # if A == B
        while accountA == accountB:
            accountA = getRandomAccount()
        # Print information
        printAvsB(accountA, accountB)

        # start guessing
        print("\n")
        guess = input("Who has more followers? 'A' or 'B'?: ").lower()
        accountAfollowerCount = int(accountA["follower_count"])
        accountBfollowerCount = int(accountB["follower_count"])
        # Clear and print logo
        clearConsole()
        print(logo)

        # Check if guess is correct
        if checkFollowers(guess, accountAfollowerCount, accountBfollowerCount):
            userScore += 1
            print(f"You were right!!Current score: {userScore}")
            shouldContinue = True
        else:
            shouldContinue = False
            print(f"Wrong! Final score: {userScore}")



#
# main
#
if __name__ == "__main__":
    clearConsole()
    GreaterOrLowerThanGame()