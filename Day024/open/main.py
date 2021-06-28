#
# Imports
#
import os

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
    # open file
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    #
    # file = open(os.path.join(__location__, "file.txt"))
    # # contents
    # contents = file.read()
    # print(contents)
    # # close file
    # file.close()

    # Best way - Read
    with open(os.path.join(__location__, "file.txt"), mode="r") as file:
        # contents
        contents = file.read()
        print(contents)

    # Write
    # with open(os.path.join(__location__, "file.txt"), mode="w") as file:
    with open(os.path.join(__location__, "file.txt"), mode="a") as file:
        file.write("\n\nNew text\n")

    # new file
    with open(os.path.join(__location__, "new_file.txt"), mode="w") as file:
        file.write("New text in new file\n")