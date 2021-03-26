#
# Imports
#
import os
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#
# Classes
#


#
# Global variables
#
is_on = True
# Create objects
coffe_machine = CoffeeMaker()
money_maker = MoneyMachine()
menu = Menu()


#
# Private functions
#

# clear_console
def clear_console():
    """
    Clears console.
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#coffe_function
def coffe_machine_function(coffee_maker, money_machine, menu):
    """

    """
    global is_on
    # Check if machine ON
    while is_on:
        # Get menu options
        options = menu.get_items()
        # Ask user to input choice
        choice = input(f"What would you like? ({options}): ")
        # Turn off
        if choice == "off":
            is_on = False
        # Report
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        # Prepare drink
        else:
            # Get info from drink to be prepared from menu
            drink = menu.find_drink(choice)
            # Check ingredients
            is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
            # Make em pay
            is_payment_successful = money_machine.make_payment(drink.cost)
            # If ingredients are enough and money enough
            if is_enough_ingredients and is_payment_successful:
                # Barista magic here:
                coffee_maker.make_coffee(drink)


#
# main
#
if __name__ == "__main__":
    clear_console()

    # Call function
    coffe_machine_function(coffe_machine, money_maker, menu)