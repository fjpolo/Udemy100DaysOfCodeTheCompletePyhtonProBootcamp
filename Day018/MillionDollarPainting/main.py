
#
# Imports
#
import os
from turtle import Turtle, Screen
import random
import colorgram

#
# Classes
#

#
# Global variables
#
directions = [0, 90, 180, 270]
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
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

# random_colour
def random_colour():
    """ 
    Returns a random rgb thruple.-
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# draw_spyrograph
def draw_spyrograph(gap_size):
    """
    Accepts a gap size and draws a spyrograph.-
    """
    for _ in range(int(360/gap_size)):
        # Spirograph
        timmy.color(random_colour())
        timmy.circle(100)
        # print(timmy.heading())
        timmy.setheading(timmy.heading() + gap_size)


# 


#
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()
    # Create Timmy
    timmy = Turtle()
    timmy.shape("turtle")
    # fullspeed
    timmy.speed(0)
    # pen up
    tim.penup()
    # hide timmy
    tim.hideturtle()

    # get colours from image.jpeg
    colours = colorgram.extract("image.jpeg", 30)
    print(colours)
    
    # Make Art
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

    #
    screen.exitonclick()