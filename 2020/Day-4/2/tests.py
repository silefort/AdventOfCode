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
        self.assertEqual(get_nb_tree(myList, 1, 1),2)
        self.assertEqual(get_nb_tree(myList, 3, 1),7)
        self.assertEqual(get_nb_tree(myList, 5, 1),3)
        self.assertEqual(get_nb_tree(myList, 7, 1),4)
        self.assertEqual(get_nb_tree(myList, 1, 2),2)
        file1.close()
        

    def test_main(self):
        self.assertEqual(main('test_input.txt'),336)

if __name__ == '__main__':
    unittest.main()
