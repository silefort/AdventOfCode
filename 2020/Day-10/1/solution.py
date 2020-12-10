def compute(joltageList):
    currentJoltage = 0
    joltageList = sorted(joltageList)
    oneSum = 0
    threeSum = 1

    for j in joltageList:
        print("--------------")
        print(currentJoltage)
        print(j)
        if j - currentJoltage == 1:
            print("diff de 1")
            oneSum += 1
        if j - currentJoltage == 3:
            print("diff de 3")
            threeSum += 1

        currentJoltage = j

    return oneSum * threeSum

def main(filename):
    file1 = open(filename, 'r')
    myList = file1.readlines()
    joltageList = []
    file1.close()
    for l in myList:
        joltageList.append(int(l))

    return compute(joltageList)

    
if __name__ == '__main__':
    solution = main('input')
    print(solution)
