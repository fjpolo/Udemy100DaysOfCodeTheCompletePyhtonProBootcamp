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

#
# main
#
if __name__ == "__main__":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

        #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
        #e.g. 
        #cipher_text = "mjqqt"
        #shift = 5
        #plain_text = "hello"
        #print output: "The decoded text is hello"


    #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
    if direction == 'encode':
        #Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
        encrypt(text, shift)
    elif direction == "decode":
        #Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
        decrypt(text, shift)
    else:
        print("Wrong choice")