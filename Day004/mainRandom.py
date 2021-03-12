#
# Imports
#
import random

#
# main
#
if __name__ == "__main__":
    # integer between 1 and 10
    random_integer = random.randint(1, 10)
    print(f"Random integer: {random_integer}")
    # float between 0 and 5 
    random_float = float(random.random() * 5)
    print(f"Random float: {random_float}")

    