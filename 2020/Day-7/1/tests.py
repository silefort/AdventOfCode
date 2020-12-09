import unittest 
from solution import *

class MyTests(unittest.TestCase):

    def test_split_line(self):
        self.assertEqual(split_line('bright gray bags contain 2 bright gold bags, 5 dull lavender bags'),('bright gray',[(2,'bright gold'),(5,'dull lavender')]))

if __name__ == '__main__':
    unittest.main()
