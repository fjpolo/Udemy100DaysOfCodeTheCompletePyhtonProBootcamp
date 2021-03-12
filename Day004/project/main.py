#
# Imports
#
import random
import sys

#
# main
#
if __name__ == "__main__":
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

    #
    # Code
    #

    # ASCII Images
    gameImages = [rock, paper, scissors]
    #Print stuff
    print("Welcome to Rock, Paper, Scissor 2.1")
    print("Menu:")
    print(" 0- Rock")
    print(" 1- Paper")
    print(" 2- Scissor")
    # User
    userChoice = int(input("Choose now:  "))
    if userChoice > 2:
        print("Invalid input...")
        sys.exit()
    print(gameImages[userChoice])
    # Computer
    computerChoice = random.randint(0, 2)
    print(f"Computer Master chose {computerChoice}")
    print(gameImages[computerChoice])
    # Game on
    if userChoice >= 3 or userChoice < 0: 
        print("You typed an invalid number, you lose!") 
    elif userChoice == 0 and computerChoice == 2:
        print("You win!")
    elif computerChoice == 0 and userChoice == 2:
        print("You lose")
    elif computerChoice > userChoice:
        print("You lose")
    elif userChoice > computerChoice:
        print("You win!")
    elif computerChoice == userChoice:
        print("It's a draw")
    
