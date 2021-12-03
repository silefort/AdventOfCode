def read_file_line_by_line(filename):
    file1 = open(filename, 'r')
    inputList = file1.readlines() 
    file1.close() 
    outputList = []
    for l in inputList:
        outputList.append(l.strip())
    return outputList

def read_file_line_by_line_to_int(filename):
    file1 = open(filename, 'r')
    inputList = file1.readlines() 
    file1.close() 
    outputList = []
    for l in inputList:
        outputList.append(int(l.strip()))
    return outputList
