import unittest 
from solution import *

class MyTests(unittest.TestCase):

    def test_is_passeport_valid(self):
        line = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd \
        byr:1937 iyr:2017 cid:147 hgt:183cm'
        self.assertEqual(is_passeport_valid(line), True)
        line = 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 \
        hcl:#cfa07d byr:1929'
        self.assertEqual(is_passeport_valid(line), False)
        line = 'iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946 hcl:#cfa07d byr:1929'
        self.assertEqual(is_passeport_valid(line), False)

    def test_is_byr_valid(self):
        self.assertEqual(is_byr_valid(2002), True)
        self.assertEqual(is_byr_valid(2003), False)

    def test_is_iyr_valid(self):
        self.assertEqual(is_iyr_valid(2012), True)
        self.assertEqual(is_iyr_valid(192), False)

    def test_is_eyr_valid(self):
        self.assertEqual(is_eyr_valid(2023), True)
        self.assertEqual(is_eyr_valid(2057), False)

    def test_is_hgt_valid(self):
        self.assertEqual(is_hgt_valid('60in'), True)
        self.assertEqual(is_hgt_valid('190cm'), True)
        self.assertEqual(is_hgt_valid('190in'), False)
        self.assertEqual(is_hgt_valid('190'), False)

    def test_is_hcl_valid(self):
        self.assertEqual(is_hcl_valid('#123abc'), True)
        self.assertEqual(is_hcl_valid('#123abz'), False)
        self.assertEqual(is_hcl_valid('123abc'), False)

    def test_is_ecl_valid(self):
        self.assertEqual(is_ecl_valid('brn'), True)
        self.assertEqual(is_ecl_valid('wat'), False)

    def test_is_pid_valid(self):
        self.assertEqual(is_pid_valid('000000001'), True)
        self.assertEqual(is_pid_valid('0123456789'), False)

    def test_parse_passeport_fields(self):
        line = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd \
        byr:1937 iyr:2017 cid:147 hgt:183cm'
        self.assertEqual(parse_passeport_fields(line), {'ecl':'gry','pid' :'860033327','eyr':'2020','hcl':'#fffffd','byr':'1937','iyr':'2017','cid':'147','hgt':'183cm'})

    # def test_main(self):
        # self.assertEqual(main('test_input.txt'),2)

if __name__ == '__main__':
    unittest.main()
