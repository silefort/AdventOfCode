import unittest 
from solution import *

class MyTests(unittest.TestCase):

    @unittest.skip("skip")
    def test_number_of_unique_answers(self):
        self.assertEqual(number_of_yes('abc'),3)
        self.assertEqual(number_of_yes('a\nb\nc'),0)
        self.assertEqual(number_of_yes('ab\nac'),1)
        self.assertEqual(number_of_yes('a\na\na\na'),1)
        self.assertEqual(number_of_yes('b\n'),1)

    def test_main(self):
       self.assertEqual(main('test_input.txt'),6)

if __name__ == '__main__':
    unittest.main()
