#
# Imports
#
import random
from art import logo
import os

#
# Global variables
#

#
# Private functions
#


# clearConsole
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# findHighestBidder
def findHighestBidder(biddingRecord):
    highestBid = 0
    winner = ""
    # loop
    for bidder in biddingRecord:
        bidAmmount = biddingRecord[bidder]
        if bidAmmount > highestBid:
            highestBid = bidAmmount
            winner = bidder
    # print winner
    print(f"The winner is: {winner} with ${highestBid}")



#
# main
#
if __name__ == "__main__":
    print(logo)
    print("Welcome to the secret auction hackware!")
    bids = {}
    biddingFinished = False
    #
    while not biddingFinished:
        name = input("What's your name?")
        price = int(input("What's your bid? $"))
        bids[name] = price
        # Continue?
        userContinue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if userContinue == "no":
            biddingFinished = True
            # Find best bid
            findHighestBidder(bids)
        elif userContinue == "yes":
            clearConsole()
