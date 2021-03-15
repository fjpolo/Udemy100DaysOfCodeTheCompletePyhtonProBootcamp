#
# Imports
#
import random
from art import logo


#
# Global variables
#
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#
# Private functions
#

#encrypt
def encrypt(start_text, shift_amount):
    cipher_text = ""
    # iterate and create ciphered text
    for char in start_text:
        cipher_text += alphabet[(alphabet.index(char) + shift_amount)%len(alphabet)]
    # print
    print(f"The encoded text is {cipher_text}")

# decrypt
def decrypt(start_text, shift_amount):
    decipher_text = ""
    # iterate and create ciphered text
    for char in start_text:
       decipher_text += alphabet[(alphabet.index(char) - shift_amount)%len(alphabet)]
    # print
    print(f"The decoded text is {decipher_text}")

#caesar
def caesar(start_text, shift_amount, cipher_direction):
    # #
    # if cipher_direction == 'encode':
    #     #Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
    #     encrypt(start_text, shift_amount)
    # elif cipher_direction == "decode":
    #     #Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
    #     decrypt(start_text, shift_amount)
    # else:
    #     print("Wrong choice")

    end_text = ""
    # if direction is not "encode" or is not "decode":
    #     print("Wrong direciton!")
    #     return 
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        #TODO-3: What happens if the user enters a number/symbol/space?
        #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    # print final text
    print(f"Here's the {cipher_direction}d result: {end_text}")

#
# main
#
if __name__ == "__main__":

    #TODO-1: Import and print the logo from art.py when the program starts.
    print(logo)

    #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
    #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
    #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
    #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
    should_end = False
    
    #
    # Loop till user is tired
    #
    while not should_end:

        # User input
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
        #Try running the program and entering a shift number of 45.
        #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
        #Hint: Think about how you can use the modulus (%).
        shift %= len(alphabet)
        
        # Call caesar
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        # Check if user wants to keep playing
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if restart == "no":
            should_end = True
            print("Goodbye")
