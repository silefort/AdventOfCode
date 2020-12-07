import re

def is_byr_valid(byr):
    return int(byr) >= 1920 and int(byr) <= 2002

def is_iyr_valid(iyr):
    return int(iyr) >= 2010 and int(iyr) <= 2020

def is_eyr_valid(eyr):
    return int(eyr) >= 2020 and int(eyr) <= 2030

def is_hgt_valid(hgt):
    if len(hgt) >= 3:
        dimension = hgt[-2:]
        height = int(hgt[:-2])

        if dimension == 'cm' and height >= 150 and height <= 193:
            return True
        
        if dimension == 'in' and height >= 59 and height <= 76:
            return True

    return False

def is_hcl_valid(hcl):
    return re.search(r'^#[0-9a-f]{6}$', hcl) is not None

def is_ecl_valid(ecl):
    return ecl in ['amb','blu','brn','gry','grn','hzl','oth']

def is_pid_valid(pid):
    return len(pid) == 9

def is_passeport_valid(line):

    myDict = parse_passeport_fields(line)
    rules = 0
    if 'byr' in myDict and is_byr_valid(myDict['byr']):
        rules += 1
    if 'iyr' in myDict and is_iyr_valid(myDict['iyr']):
        rules += 1
    if 'eyr' in myDict and is_eyr_valid(myDict['eyr']):
        rules += 1
    if 'hgt' in myDict and is_hgt_valid(myDict['hgt']):
        rules += 1
    if 'hcl' in myDict and is_hcl_valid(myDict['hcl']):
        rules += 1
    if 'ecl' in myDict and is_ecl_valid(myDict['ecl']):
        rules += 1
    if 'pid' in myDict and is_pid_valid(myDict['pid']):
        rules += 1
    return rules == 7

def parse_passeport_fields(line):
    myDict = {}
    line = line.split(' ')
    for l in line:
        if l != '':
            myDict[l.split(':')[0]] = l.split(':')[1]

    return myDict

def main(filename):
    file1 = open(filename, 'r')
    myList = file1.read().split('\n\n')
    total = 0
    for passeport in myList:
        if is_passeport_valid(passeport.replace("\n"," ")):
            total += 1
    file1.close()

    return total
        
if __name__ == '__main__':
    solution = main('input')
    print(solution)
