import unittest 
from solution import *

class MyTests(unittest.TestCase):

    def test_decode_row_number(self):
        self.assertEqual(decode_row_number('BFFFBBF'), 70)
        self.assertEqual(decode_row_number('FFFBBBF'), 14)
        self.assertEqual(decode_row_number('BBFFBBF'), 102)

    def test_decode_column_number(self):
        self.assertEqual(decode_column_number('RRR'), 7)
        self.assertEqual(decode_column_number('RLL'), 4)

    def test_decode_seat_id(self):
        self.assertEqual(decode_seat_id('BFFFBBFRRR'), 567)
        self.assertEqual(decode_seat_id('FFFBBBFRRR'), 119)
        self.assertEqual(decode_seat_id('BBFFBBFRLL'), 820)

    def test_find_max_seat_id(self):
        self.assertEqual(find_max_seat_id('test_input.txt'),820)

    # def test_main(self):
        # self.assertEqual(main('test_input.txt'),2)

if __name__ == '__main__':
    unittest.main()
