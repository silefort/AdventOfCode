import unittest 
from solution import *

class MyTests(unittest.TestCase):

    def test_number_of_unique_answers(self):
        self.assertEqual(number_of_unique_answers('abc'),3)
        self.assertEqual(number_of_unique_answers('abc\na\nb'),3)
        self.assertEqual(number_of_unique_answers('a\na\na\na'),1)

    def test_main(self):
       self.assertEqual(main('test_input.txt'),11)

if __name__ == '__main__':
    unittest.main()
