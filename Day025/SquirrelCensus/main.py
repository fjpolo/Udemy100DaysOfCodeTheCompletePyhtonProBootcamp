
#
# Imports
#
import os
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

    # Read CSV
    data = pd.read_csv("Day025/SquirrelCensus/Census.csv")

    # Red
    red_data = data[data["Primary Fur Color"] == "Cinnamon"]
    red_count = len(red_data)

    # Grey
    grey_data = data[data["Primary Fur Color"] == "Gray"]
    grey_count = len(grey_data)

    # Black
    black_data = data[data["Primary Fur Color"] == "Black"]
    black_count = len(black_data)


    # Save CSv
    data_dict = {
        "Fur Colour":["grey", "red", "black"],
        "Count": [grey_count, red_count, black_count] 
    }
    data_new = pd.DataFrame(data_dict)
    data_new.to_csv("Day025/SquirrelCensus/squirrel_count.csv")