#
# Imports
#
import random

#
# Private functions
#

# add
def add(a, b):
    return a + b
# subtract
def subtract(a, b):
    return a - b
# multiply
def multiply(a, b):
    return a * b
# divide
def divide(numerator, denominator):
    return float(numerator) / denominator

# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
    print("Hello!")
    print("Welcome to the jungle")
    print("We've got fun and games")


#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#
# main
#
if __name__ == "__main__":
    print("This is main")
    # call greet()
    greet()
    print("This is main again")
    # Greet with a name
    print("Now greet with a name")
    greet_with_name("Juan José de la Veracruz y todos los Santos")
    #
    print("Now even betta")
    greet_with("Paca la Piranha", "Madriz")
    print("Wow...amazing!")

