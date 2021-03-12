"""
You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name
"""
    #
    # Imports
    #
    import random

    #
    # main
    #
    if __name__ == "__main__":
    # Split string method
    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(", ")
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇
    #print(names)
    # number of people
    people = len(names)
    # random choice
    choice = random.randint(0, (people-1))
    # print chosen one
    print( names[choice] + " will pay.-")