import numpy as np

def decode_row_number(passId):
    binaryPass = passId.replace('B','1').replace('F','0')
    return int(binaryPass,2)

def decode_column_number(passId):
    binaryPass = passId.replace('R','1').replace('L','0')
    return int(binaryPass,2)

def decode_seat_id(passId):
    return decode_row_number(passId[:7]) * 8 + decode_column_number(passId[7:])

def find_max_seat_id(filename):
    file1 = open(filename, 'r')
    myList = file1.readlines()
    maxId = 0
    for l in myList:
        if decode_seat_id(l) > maxId:
            maxId = decode_seat_id(l)

    file1.close()
    return maxId

def find_empty_seats(filename):
    matrix = np.ones((128,8))

    file1 = open(filename, 'r')
    myList = file1.readlines()
    for l in myList:
        matrix[decode_row_number(l[:7])][decode_column_number(l[7:])] = 0

    print(matrix)
    print(np.transpose([np.nonzero(matrix)]))
    file1.close()
    return 820


def main(filename):
    return find_empty_seats(filename)

if __name__ == '__main__':
    solution = main('input')
    print(solution)
