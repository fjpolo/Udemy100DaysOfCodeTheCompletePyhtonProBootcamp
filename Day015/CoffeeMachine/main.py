
#
# Imports
#
import os
from menu import MENU
#
# Global variables
#
isOn = True
profit = 0
resources = {
                "water": 300,
                "milk": 200,
                "coffee": 100,
            }

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

# TurnOff
def TurnOff():
    """
    Turns machine off
    """
    global isOn
    isOn = False

# checkResourcesEnough
def checkResourcesEnough(ingredients):
    """
    Checks if available resources are enough.-
    """
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f("Not enouugh {item}"))
            return False
    return True

# processPayment
def processPayment():
    """
    Returns the total calculated from coins inserted.
    """
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# isPaymentEnough
def isPaymentEnough(payment, cost):
    """
    Returns true if money is enough, otherwise false.-
    """
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"There we go, here's your change: ${change}")
        # now modify profit
        global profit
        profit += cost
        return True
    # You poor bastard
    else:
        print("Not enough moneys mate.-")
        return False
    
# BaristaMagic
def BaristaMagic(drinkName, drinkIngredients):
    """
    Takes the name of the drink and ingredients, and makes the magic.-
    """    
    for item in drinkIngredients:
        resources[item] -= drinkIngredients[item]
    print(f"Here is your {drinkName} ☕️. Enjoy!")
    print('\n')

# PrintReport
def PrintReport():
    """
    Prints a full report.-
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
    print('\n')


# declare here to have function names available
availableCommands = {
                        "off":TurnOff,
                        "report":PrintReport
                    }
                    
#CoffeeMachine
def CoffeMachine():
    # While ON
    while isOn:
        # Ask for coffee type
        choice = input("What would you like? (espresso/latte/cappuccino/off/report): ").lower()
        # Check if off
        if choice == 'off':
            availableCommands[choice]()
        # Check if report
        elif choice == "report":
            availableCommands[choice]()
        # Coffess
        else:
            drink = MENU[choice]
            # Enough moneys?
            if checkResourcesEnough(drink["ingredients"]):
                # Make the user pay
                pay = processPayment()
                # Process transaction
                if isPaymentEnough(pay, drink["cost"]):
                    # Make drink
                    BaristaMagic(choice, drink["ingredients"])




#
# main
#
if __name__ == "__main__":
    clearConsole()
    CoffeMachine()