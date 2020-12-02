def sum_is_2020(x,y):
    return x+y == 2020

def find_2_entries(myList):
    i = 0
    j = 0
    for current_i in myList:
        for current_j in myList:
            if current_i + current_j == 2020:
                i = current_i
                j = current_j
    return i*j

def read_file_line_by_line(filename):
    file1 = open(filename, 'r')
    myList = file1.readlines() 

    myIntList = []
    for i in myList:
        myIntList.append(int(i))
    file1.close() 
    return myIntList

def main(filename):
    myList = read_file_line_by_line(filename)
    return find_2_entries(myList)

if __name__ == '__main__':
    solution = main('input')
    print(solution)
