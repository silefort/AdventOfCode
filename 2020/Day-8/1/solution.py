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
    print("acc= " + str(acc) + ", index= ", str(index))
    return (acc,index)

def exec_code(filename):
    file1 = open(filename, 'r')
    myList = file1.readlines()
    file1.close()
    indexes = []
    acc = 0
    index = 0
    while index not in indexes:
        indexes.append(index)
        acc, index = exec_line(acc, index, myList)
    return acc

if __name__ == '__main__':
    solution = exec_code('input')
    print(solution)
