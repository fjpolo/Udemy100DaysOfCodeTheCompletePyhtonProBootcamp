0
#
# Imports
#
import os
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

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
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


#
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()
    # Create question_bank
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(q_text = question_text, q_answer = question_answer)
        question_bank.append(new_question)
    
    # Print list of objects
    # print(question_bank)
    
    # Create a QuizBrain object
    quiz_brain = QuizBrain(question_bank)
    # Ask question
    while quiz_brain.still_has_questions(): 
        quiz_brain.next_question()

    # 
    print("You have completed the quiz!")
    print(f"Your final score is: {quiz_brain.score}/{quiz_brain.question_number}")


        