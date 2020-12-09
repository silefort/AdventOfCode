def search_for_sum(numList,value):
    res = False
    for i in numList:
        for j in numList:
            # if ( i+j == int(value)) and (i != j):
            if ( int(i)+int(j) == int(value)) and (int(i) != int(j)):
                res = True
                break
    return res

def main(filename):
    file1 = open(filename, 'r')
    myList = file1.readlines()
    file1.close()
    i = 25
    found = False
    while not found:
        currentValue = int(myList[i].strip())
        currentList = myList[i-25:i]
        found = not search_for_sum(currentList,currentValue)
        i+=1
    return myList[i-1]
    
if __name__ == '__main__':
    solution = main('input')
    print(solution)
