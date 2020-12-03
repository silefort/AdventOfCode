import unittest 
from solution import *

class MyTests(unittest.TestCase):

    def test_get_case(self):
        line = '..##.......'
        self.assertEqual(get_case(line, 3),'#')
        self.assertEqual(get_case(line, 14),'#')
        self.assertEqual(get_case(line, 16),'.')
        line = '.#...##..#.'
        self.assertEqual(get_case(line, 12),'#')

    def test_get_nb_tree(self):
        file1 = open('test_input.txt', 'r')
        myList = file1.readlines()
        self.assertEqual(get_nb_tree(myList, 3, 1),7)
        file1.close()
        

    def test_main(self):
        self.assertEqual(main('test_input.txt'),7)

if __name__ == '__main__':
    unittest.main()
