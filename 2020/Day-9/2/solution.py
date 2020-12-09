def search_for_sum(numList,value):
    res = False
    for i in numList:
        for j in numList:
            # if ( i+j == int(value)) and (i != j):
            if ( int(i)+int(j) == int(value)) and (int(i) != int(j)):
                res = True
                break
    return res

def add_list(numList):
    res = 0
    for i in numList:
        res += int(i)
    return res


def main(filename):
    file1 = open(filename, 'r')
    myList = file1.readlines()
    file1.close()
    res = 41682220 
    found = False
    firstIndex = 0
    while not found and firstIndex < len(myList):
        sumSize = 2
        total = 0
        while int(total) < int(res):
            currentList = myList[firstIndex:firstIndex+sumSize]
            total = add_list(currentList)
            found = (total == res)
            # print("-------------------")
            # print(currentList)
            # print(firstIndex)
            # print(sumSize)
            sumSize += 1
        firstIndex += 1

    return (int(min(currentList)) + int(max(currentList)))
    
if __name__ == '__main__':
    solution = main('input')
    print(solution)
