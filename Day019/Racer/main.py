
#
# Imports
#
import os
from turtle import Turtle, Screen
import random

#
# Classes
#

#
# Global variables
#    
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-75, -45, -15, 15, 45, 75]


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

#
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()

    # flag
    is_race_on = False

    # Create screen
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    # Ask the user to bet
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race. Enter a color: ")


    # Create turtles
    all_turtles = []
    for turtle_index in range(0, 6):         
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-240, y=y_positions[turtle_index])
        # append to list
        all_turtles.append(new_turtle)
    
    # Chekc if bet
    if user_bet:
        is_race_on = True

    # As long as game on
    while is_race_on:
        # Loop through turtles
        for turtle in all_turtles:
            # Chek limits
            if turtle.xcor() > 230:
                # Stop race
                is_race_on = False
                # Winner!
                winning_color = turtle.pencolor()
                # bet
                if winning_color == user_bet:
                    print("Winner!")
                else:
                    print("Loser")
                    print(f"{winning_color} won!")
            random_distance = random.randint(0,10)
            turtle.forward(random_distance)
        


    # Exit on click
    screen.exitonclick()
