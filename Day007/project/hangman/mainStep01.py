#
# Imports
#
import random

#
# main
#
if __name__ == "__main__":
    #Step 1 

    word_list = ["aardvark", "baboon", "camel"]

    #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
   #  randomIndex = random.randint(0, (len(word_list)-1))
    randomIdex = random.choice(word_list)
    chosenWord = word_list[randomIndex]
    # print(chosenWord)

    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter:  ").lower()
    # print(guess)
    
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for letter in chosenWord:
        if letter  == guess:
            print("Right!")
        else:
            print("Wrong!")        