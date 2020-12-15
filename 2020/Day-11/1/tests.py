import unittest 
import numpy as np
from solution import *

class MyTests(unittest.TestCase):

    def test_count_char_in_string(self):
        self.assertEqual(count_char_in_string('L#..#L','L'),2)

    def test_read_file(self):
        self.assertEqual(read_file('test_input_1.txt'),['L#.','.#L'])

    def test_next_status(self):
        self.assertEqual(next_status(read_file('test_input.txt'),0,0),'#')
        self.assertEqual(next_status(read_file('test_input.txt'),2,1),'#')
        self.assertEqual(next_status(read_file('test_input_2.txt'),6,0),'#')

    def test_get_adjacent(self):
        self.assertEqual(get_adjacent(read_file('test_input.txt'),0,0),'.LL')
        self.assertEqual(get_adjacent(read_file('test_input.txt'),1,1),'L.LLLL.L')
        self.assertEqual(get_adjacent(read_file('test_input_2.txt'),3,3),'#.##.##.')

    def test_get_next_round(self):
        self.assertEqual(get_next_round(read_file('test_input.txt')),['#.##.##.##','#######.##','#.#.#..#..','####.##.##','#.##.##.##','#.#####.##','..#.#.....','##########','#.######.#','#.#####.##'])
        self.assertEqual(get_next_round(read_file('test_input_2.txt')),['#.LL.L#.##','#LLLLLL.L#','L.L.L..L..','#LLL.LL.L#','#.LL.LL.LL','#.LLLL#.##','..L.L.....','#LLLLLLLL#','#.LLLLLL.L','#.#LLLL.##'])

    def test_search(self):
        self.assertEqual(search(read_file('test_input.txt')),37)

    # def test_main(self):
            # self.assertEqual(main('test_input.txt'),22*10)

if __name__ == '__main__':
    unittest.main()
