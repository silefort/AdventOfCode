import unittest 
from solution import *

class MyTests(unittest.TestCase):

    def test_is_password_legit(self):
        self.assertEqual(is_password_legit(1, 3, 'a', 'abcde'), True)
        self.assertEqual(is_password_legit(1, 3, 'b', 'cdefg'), False)
        self.assertEqual(is_password_legit(2, 9, 'c', 'ccccccccc'), True)

    def test_count_iteration(self):
        self.assertEqual(count_iteration('a','abcde'),1)
        self.assertEqual(count_iteration('b','cdefg'),0)

    def test_main(self):
        self.assertEqual(main('test_input.txt'),2)

if __name__ == '__main__':
    unittest.main()
