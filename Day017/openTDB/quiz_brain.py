#
# Imports
#
import unittest

#
# class QuizBrain
#
class QuizBrain:
    """
    Takes a questions list, and returns a question.-
    """
    # Constructor()
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0
    # next_question()
    def next_question(self):
        """
        Retrieve item at current question number from the question list.-
        """
        current_question = self.questions_list[self.question_number]
        if self.still_has_questions():
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {current_question.text} 'True' or 'False': ")
            self.check_answer(user_answer, current_question.answer)
        else:
            print("No more questions...")
    # still_has_questions()
    def still_has_questions(self):
        """
        Returns bool True if there are questions remaining, else returns False.- 
        """
        # if self.question_number < len(self.questions_list):
        #     return True
        # else:
        #     return False
        return self.question_number < len(self.questions_list)
    # check_answer()
    def check_answer(self, user_answer, correct_answer):
        """
        Lets the user know if the answer was correct or incorrect.-
        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong answer...")
        print(f"The correct answer was: {correct_answer}")
        print(f"The current score is: {self.score}/{self.question_number}")



#
# Global variables
#
test_question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
]

#
# Testing
#

# TestQuizBrain
class TestQuizBrain(unittest.TestCase):
    """
    Tests QuizBrain class.-
    """
    def test_QuizBrain__constructor(self):
        """
        Test QuizBrain constructor.-
        """
        test_QuizBrain = QuizBrain(test_question_data)
        self.assertEqual( test_QuizBrain.question_number, 0)
        for _ in range(0, 3):
            self.assertEqual(test_QuizBrain.questions_list[_]["text"], test_question_data[_]["text"])        
    #
    def test_QuizBrain__still_has_questions(self):
        """
        Test QuizBrain still_has_questions() method.-
        """
        test_QuizBrain = QuizBrain(test_question_data)
        self.assertEqual( test_QuizBrain.still_has_questions(), True)
        test_QuizBrain = QuizBrain(test_question_data)
        self.assertEqual( test_QuizBrain.still_has_questions(), True)
        test_QuizBrain = QuizBrain(test_question_data)
        self.assertEqual( test_QuizBrain.still_has_questions(), True)




# Call testing
# unittest.main()