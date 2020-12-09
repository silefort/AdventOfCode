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
        self.assertEqual(exec_code('test_input.txt'),5)

if __name__ == '__main__':
    unittest.main()
