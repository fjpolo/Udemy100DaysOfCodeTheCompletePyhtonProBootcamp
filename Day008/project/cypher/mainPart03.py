#
# Imports
#
import random

#
# Global variables
#
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#
# Private functions
#

#encrypt
def encrypt(text, shift):
    cipher_text = ""
    # iterate and create ciphered text
    for letter in text:
        cipher_text += alphabet[(alphabet.index(letter) + shift)%len(alphabet)]
    # print
    print(f"The encoded text is {cipher_text}")

# decrypt
def decrypt(text, shift):
    decipher_text = ""
    # iterate and create ciphered text
    for letter in text:
       decipher_text += alphabet[(alphabet.index(letter) - shift)%len(alphabet)]
    # print
    print(f"The decoded text is {decipher_text}")

#caesar
def caesar(text, shift, direction):
    if direction == 'encode':
        #Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
        encrypt(text, shift)
    elif direction == "decode":
        #Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
        decrypt(text, shift)
    else:
        print("Wrong choice")

#
# main
#
if __name__ == "__main__":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
    #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    caesar(text, shift, direction)