import unittest 
from solution import *

class MyTests(unittest.TestCase):

    def test_compute(self):
        joltageList = [16,10,15,5,1,11,7,19,6,12,4]
        self.assertEqual(compute(joltageList),35)

    def test_main(self):
        self.assertEqual(main('test_input.txt'),22*10)

if __name__ == '__main__':
    unittest.main()
