#
# Imports
#
import random

#
# main
#
if __name__ == "__main__":
    statesOfMyHouse = ["Lobby", "Kitchen", "Living room", "Bedroom"]
    statesOfMyHouse.append("Loo")
    thingsOfMyHouse = ["Floor", "Windows", "Doors", "Ceiling"]
    statesOfMyHouse.extend(thingsOfMyHouse)
    print(statesOfMyHouse)

