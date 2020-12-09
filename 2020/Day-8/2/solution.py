def parse_line(line):
    return (line.split(' ')[0], int(line.split(' ')[1]))

def exec_line(acc,index,myLines):
    currentLine = myLines[index]
    operation, argument = parse_line(currentLine)
    if operation == 'nop':
        index+=1
    if operation == 'jmp':
        index+=argument
    if operation == 'acc':
        index+=1
        acc+=argument
    # print("acc= " + str(acc) + ", index= ", str(index))
    return (acc,index)

def exec_code(myList):
    indexes = []
    acc = 0
    index = 0
    while index not in indexes and index != (len(myList) -1):
        indexes.append(index)
        acc, index = exec_line(acc, index, myList)
    print(index)
    return acc, index

def find_next_change(myList,lastChangeIndex):
    i = lastChangeIndex + 1
    found = False
    while i < len(myList) and not found:
        if parse_line(myList[i])[0] == 'jmp' or parse_line(myList[i])[0] == 'nop':
            found = True
        i += 1
    return (i-1)

def swap_nop_jmp(line):
    if "jmp" in line:
        return line.replace('jmp','nop')
    if "nop" in line:
        return line.replace('nop','jmp')

def main(filename):
    file1 = open(filename, 'r')
    myList = file1.readlines()
    file1.close()

    lastindex = 0
    currentChangeIndex = -1
    while lastindex != (len(myList) -1):
        currentChangeIndex = find_next_change(myList,currentChangeIndex)
        print("currentChangeIndex= ", currentChangeIndex)
        myList[currentChangeIndex] = swap_nop_jmp(myList[currentChangeIndex])
        print(myList)
        acc, lastindex = exec_code(myList)
        myList[currentChangeIndex] = swap_nop_jmp(myList[currentChangeIndex])
        print("lastindex= ", lastindex)
        print("acc= ",acc)

    return acc


if __name__ == '__main__':
    solution = main('input')
    print(solution)
