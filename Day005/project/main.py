#
# Imports
#
import random

#
# main
#
if __name__ == "__main__":
    # Variables
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    # # Empty password
    # password = ""
    # # Add letters
    # for letter in range(1, nr_letters+1):
    #     password += random.choice(letters)
    # # Add symbols
    # for symbol in range(1, nr_symbols+1):
    #     password += random.choice(symbols)
    # # Add numbers
    # for number in range(1, nr_numbers+1):
    #     password += random.choice(symbols)
    # # Print password
    # print(password)


    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    # Empty password list
    passwordList = []
    # Random letters
    for char in range(1, nr_letters + 1):
      passwordList.append(random.choice(letters))
    # Random symbols
    for char in range(1, nr_symbols + 1):
        passwordList += random.choice(symbols)
    # Random numbers
    for char in range(1, nr_numbers + 1):
        passwordList += random.choice(numbers)
    # Print password list
    print(passwordList)
    # Randomize
    random.shuffle(passwordList)
    # Print randomized password list
    print(passwordList)
    # Empty password
    password = ""
    for char in passwordList:
        password += char
    # Password list
    print(f"Your password is: {password}")
