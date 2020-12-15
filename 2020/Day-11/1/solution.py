def next_status(myFile,i,j):
    # print(i)
    # print(j)
    current = myFile[j][i]
    nextStatus = current
    adjacent = get_adjacent(myFile,i,j)
    # print("current=" + current)
    # print("adjacent=" + adjacent)
    if current == 'L' and count_char_in_string(adjacent,'#') == 0:
        nextStatus = '#'
    if current == '#' and count_char_in_string(adjacent,'#') >= 4:
        nextStatus = 'L'
    return nextStatus

def count_char_in_string(myString,myChar):
    count = 0
    for c in myString:
        if c == myChar:
            count += 1
    return count

def get_adjacent(myFile,i,j):
    myStr = ''
    # print("----- i=" + str(i) + " j=" + str(j))
    for b in range(j-1,j+2):
        for a in range(i-1,i+2):
            if a>=0 and b>=0 and a<len(myFile[0]) and b<len(myFile):
                if a == i and b == j:
                    myStr = myStr
                else:
                    myStr += myFile[b][a]
                    # print("a=" + str(a) + " b=" + str(b) + " current=" + myFile[b][a])
    return myStr

def get_next_round(myFile):
    outputFile = []
    for j in range(len(myFile)):
        currentLine = ''
        for i in range(len(myFile[0])):
            currentLine += next_status(myFile,i,j)
        outputFile.append(currentLine)

    return outputFile

def search(myFile):
    currentRound = myFile
    found = False
    while not found:
        nextRound = get_next_round(currentRound)
        if nextRound == currentRound:
            found = True
        print(nextRound)
        currentRound = nextRound

    return occupied_seats(currentRound)
    
def read_file(filename):
    file1 = open(filename, 'r')
    myFile = file1.read().splitlines()
    file1.close()
    return myFile

def occupied_seats(myFile):
    total = 0
    for i in myFile:
        total += count_char_in_string(i,'#')

    return total



if __name__ == '__main__':
    print(search(read_file('input')))
