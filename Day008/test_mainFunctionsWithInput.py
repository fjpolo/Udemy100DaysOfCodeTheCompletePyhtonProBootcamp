"""
https://www.blog.pythonlibrary.org/2016/07/07/python-3-testing-an-intro-to-unittest/
"""
#
# Import
# 
import mainFunctionsWithInput
import unittest


#
# Private unit tests
#

# TestAdd
class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = mainFunctionsWithInput.add(1, 2)
        self.assertEqual(result, 3)
    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = mainFunctionsWithInput.add(10.5, 2)
        self.assertEqual(result, 12.5)
    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = mainFunctionsWithInput.add('abc', 'def')
        self.assertEqual(result, 'abcdef')

#
# main
#
if __name__ == "__main__":
    print("This is main")


    #
    print("Testing")
    unittest.main()