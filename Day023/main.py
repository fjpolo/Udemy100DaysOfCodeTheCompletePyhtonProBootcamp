#
# Imports
#
import os
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#
# Classes
#

#
# Global variables
#

#
# Private functions
#

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
    # Screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    # Player
    player = Player()
    # Move player
    screen.listen()
    screen.onkey(player.go_up, "Up")
    screen.onkey(player.go_down, "Down")
    # Cars
    car_manager = CarManager()
    # Scoreboard
    scoreboard = Scoreboard()
    # Game On
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        # create and move cars
        car_manager.create_car()
        car_manager.move_cars()
        # collission
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()
        # Cross
        if player.is_at_finish_line():
            # get back to starting position
            player.got_to_start()
            # next level
            car_manager.level_up()
            #
            scoreboard.increase_level()
    #
    screen.exitonclick()