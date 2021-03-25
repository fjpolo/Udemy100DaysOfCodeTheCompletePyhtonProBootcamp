
#
# Imports
#
import os

#
# Global variables
#
enemies = 1
game_level  = 3

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

#increase_enemies
def increase_enemies():
    """
    Increase local enemy count.-
    """
    enemies = 2
    print(f"enemies inside function: {enemies}")

#
# main
#
if __name__ == "__main__":
    increase_enemies()
    print(f"enemies outside function: {enemies}")
