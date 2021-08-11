#
# Imports
#
import os
import turtle
import pandas as pd


#
# Classes
#

#
# Global variables
#

#
# Private functions
#

#
def get_mouse_click_coord(x, y):
    """"""
    print(x, y)
    turtle.onscreenclick(get_mouse_click_coord)
    turtle.mainloop()


# clear_console
def clear_console():
    """
    Clears console.
    """
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


#
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()

    # Graphs
    screen = turtle.Screen()
    screen.title("Yanki States Game")
    image = "Day025/YankiStates/blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    # Read CSV
    data = pd.read_csv("Day025/YankiStates/50_states.csv")
    states = data.state.to_list()

    # loop
    guessed_states = []

    while len(guessed_states) < 50:
        # Answer
        answer_state = screen.textinput(
            title=f"{len(guessed_states)}/50 States",
            prompt="What's another state's name?",
        ).title()

        # exit
        if answer_state == "Exit":
            missing_states = [state for state in states if state not in guessed_states]
            # for state in states:
            #     if state not in guessed_states:
            #         missing_states.append(state)
            new_data = pd.DataFrame(missing_states)
            new_data.to_csv("Day026/YankiStates/states_to_learn.csv")
            break

        # Check correct
        if answer_state in states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(state_data.state.item())
            guessed_states.append(answer_state)
