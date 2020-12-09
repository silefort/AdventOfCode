import unittest 
from solution import *

class MyTests(unittest.TestCase):

    def test_split_line(self):
        self.assertEqual(split_line('bright gray bags contain 2 bright gold bags, 5 dull lavender bags'),('bright gray',[(2,'bright gold'),(5,'dull lavender')]))
        self.assertEqual(split_line('striped orange bags contain no other bags.'),('striped orange',[]))

    def test_get_number_bags(self):
        # myLines = ['striped orange bags contain no other bags','shiny gold bags contain 1 faded blue bag, 2 striped orange bags.','faded blue bags contain no other bags']
        # self.assertEqual(get_number_bags(myLines, 'shiny gold'),3)
        # myLines = ['shiny gold bags contain 2 dark red bags.','dark red bags contain 2 dark orange bags.','dark orange bags contain 2 dark yellow bags.','dark yellow bags contain 2 dark green bags.','dark green bags contain 2 dark blue bags.','dark blue bags contain 2 dark violet bags.','dark violet bags contain no other bags.']
        myLines = ['shiny gold bags contain 2 dark red bags.',
                'dark red bags contain 2 dark orange bags.',
                'dark orange bags contain 2 dark yellow bags.',
                'dark yellow bags contain 2 dark green bags.',
                'dark green bags contain 2 dark blue bags.',
                'dark blue bags contain 2 dark violet bags.',
                'dark violet bags contain no other bags.']
        self.assertEqual(get_number_bags(myLines, 'shiny gold'),126)
        self.assertEqual(get_number_bags(myLines, 'dark violet'),0)
        self.assertEqual(get_number_bags(myLines, 'dark blue'),2)
        self.assertEqual(get_number_bags(myLines, 'dark green'),6)

    def test_main(self):
        self.assertEqual(main('test_input.txt'),32)

if __name__ == '__main__':
    unittest.main()
