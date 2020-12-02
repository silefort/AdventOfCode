import unittest 
from solution import *

class MyTests(unittest.TestCase):

    def test_sum_up_1010_and_1010_to_2020(self):  
        self.assertEqual(sum_is_2020(1010,1010), True)

    def test_sum_up_1_and_2019_to_2020(self):  
        self.assertEqual(sum_is_2020(1,2019), True)

    def test_sum_up_1_and_2_not_to_2020(self):  
        self.assertEqual(sum_is_2020(1,2), False)

    def test_find_2_items_in_list(self):
        myList = [1,2,3,4,1009,1011]
        self.assertEqual(find_2_entries(myList),1009*1011)

    def test_read_file(self):
        self.assertEqual(read_file_line_by_line('test_input.txt'),[1,2,1009,1011])

    def test_main(self):
        self.assertEqual(main('test_input.txt'),1009*1011)

if __name__ == '__main__':
    unittest.main()
