
#
# Imports
#
import os
from  prettytable import PrettyTable

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
    clear_console()
    # Create new table
    table = PrettyTable()
    # print object
    print(table)
    # Add info
    table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"] )
    table.add_column("Type", ["Electric", "Water", "Fire"])
    # print object
    print(table)
    # Change appearence
    table.align = "l"
    # print object
    print(table)