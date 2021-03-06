#
# main
#
if __name__ == "__main__":
    #If the bill was $150.00, split between 5 people, with 12% tip. 
    #Each person should pay (150.00 / 5) * 1.12 = 33.6
    #Format the result to 2 decimal places = 33.60
    #Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
    #HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
    #HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

    print("Welcome to Tipulator 3.2")
    billTotal = float(input("What was the total bill? $"))
    tip = int(input("What tip would you like to give? 10, 12 or 15? %"))
    nrPeople = int(input("How many people to split it?"))
    # Calculate and print
    #print("Each person should pay $", float( round(float(billTotal) * (float(float(100)+float(tip))/float(100)) / float(nrPeople), 2 ) ) )
    tipPercentage = tip / 100.0
    TotalTipAmount = billTotal * tipPercentage
    totalBill = billTotal + TotalTipAmount
    billPerPerson = totalBill / nrPeople
    finalAmmount = round( billPerPerson, 2 )
    finalAmmount = "{:.2f}".format(billPerPerson)
    print(f"Each person should pay ${finalAmmount}")