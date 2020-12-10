import unittest 
from solution import *

class MyTests(unittest.TestCase):
    def test_search_for_sum(self):
        numList = ['1','2','3']
        self.assertEqual(search_for_sum(numList,4),True)

    def test_main(self):
        print(main('test_input.txt'))

if __name__ == '__main__':
    unittest.main()
