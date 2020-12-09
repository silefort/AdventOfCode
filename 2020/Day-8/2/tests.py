import unittest 
from solution import *

class MyTests(unittest.TestCase):

    @unittest.skip("skip")
    def test_parse_line(self):
        self.assertEqual(parse_line('acc +1'),('acc',1))
        self.assertEqual(parse_line('jmp -1'),('jmp',-1))

    @unittest.skip("skip")
    def test_exec_line(self):
        myLines=['nop +0','jmp -3']
        self.assertEqual(exec_line(0,0,myLines),(0,1))
        self.assertEqual(exec_line(2,1,myLines),(2,-2))

    def test_exec_code(self):
        file1 = open('test_input.txt', 'r')
        myList = file1.readlines()
        file1.close()
        self.assertEqual(exec_code(myList),8)

    def test_find_next_change(self):
        file1 = open('test_input.txt', 'r')
        myList = file1.readlines()
        file1.close()
        self.assertEqual(find_next_change(myList,-1),0)
        self.assertEqual(find_next_change(myList,1),2)

    def test_main(self):
        self.assertEqual(main('test_input.txt'),8)

if __name__ == '__main__':
    unittest.main()
