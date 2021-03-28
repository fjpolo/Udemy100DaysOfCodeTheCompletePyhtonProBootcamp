#
# Imports
#
import unittest

#
# class Question
#
class Question:
    """
    Holds a question and its answer.-
    """
    # Constructor
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


#
# Testing
#

# TestQuestion
class TestQuestion(unittest.TestCase):
    """
    Tests Question class.-
    """
    def test_add_question(self):
        """
        Test that a question and its answer are being saved in an aóbject.-
        """
        testQuestion = Question("Is True True?", "True")
        self.assertEqual(testQuestion.text, "Is True True?")
        self.assertEqual(testQuestion.answer, "True")


# Call testing
# unittest.main()