import sys 
sys.path.append('..')
import tools.fileManipulation as fileManipulation
from operator import xor

def get_output_values(line):
    return (line.split('| ')[1]).split(' ')

def get_input_values(line):
    return (line.split(' | ')[0]).split(' ')

def find_7(line):
    for i in range(0, len(line)):
        if len(line[i]) == 3:
            return i

def find_1(line):
    for i in range(0, len(line)):
        if len(line[i]) == 2:
            return i

def find_4(line):
    for i in range(0, len(line)):
        if len(line[i]) == 4:
            return i

def find_8(line):
    for i in range(0, len(line)):
        if len(line[i]) == 7:
            return i

def find_5(line):
    val1 = line[find_1(line)]
    val4 = line[find_4(line)]
    sub4 = substract(val1, val4)
    for i in range(0, len(line)):
        if len(line[i]) == 5 and sub4[0] in line[i] and sub4[1] in line[i] and xor((val1[0] in line[i]),(val1[1] in line[i])):
            return i

def find_3(line):
    val1 = line[find_1(line)]
    val4 = line[find_4(line)]
    sub4 = substract(val1, val4)
    for i in range(0, len(line)):
        if len(line[i]) == 5 and val1[0] in line[i] and val1[1] in line[i] and xor((sub4[0] in line[i]),(sub4[1] in line[i])):
            return i

def find_2(line):
    val3 = line[find_3(line)]
    val5 = line[find_5(line)]
    for i in range(0, len(line)):
        if len(line[i]) == 5 and val3 != line[i] and val5 != line[i]:
            return i

def find_6(line):
    val1 = line[find_1(line)]
    for i in range(0, len(line)):
        if len(line[i]) == 6 and xor((val1[0] in line[i]),(val1[1] in line[i])):
            return i

def find_0(line):
    val1 = line[find_1(line)]
    val4 = line[find_4(line)]
    sub4 = substract(val1, val4)
    for i in range(0, len(line)):
        if len(line[i]) == 6 and xor((sub4[0] in line[i]),(sub4[1] in line[i])):
            return i

def find_9(line):
    val4 = line[find_4(line)]
    for i in range(0, len(line)):
        if len(line[i]) == 6 and val4[0] in line[i] and val4[1] in line[i] and val4[2] in line[i] and val4[3] in line[i]:
            return i

def substract(val1, val2):
    output = []
    for i in val2:
        if val1.count(i) == 0:
            output.append(i)

    return output

def find_values(line):
    values = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    values[find_1(line)] = 1
    values[find_4(line)] = 4
    values[find_7(line)] = 7
    values[find_8(line)] = 8
    values[find_5(line)] = 5
    values[find_2(line)] = 2
    values[find_3(line)] = 3
    values[find_6(line)] = 6
    values[find_0(line)] = 0
    values[find_9(line)] = 9

    return values

def get_output_digits(line):

    outputValues = get_output_values(line)
    inputValues = get_input_values(line)
    inputValuesSorted = []
    for i in inputValues:
        inputValuesSorted.append(sorted(i))
    inputDigits = find_values(inputValues)
    resultat = []
    for i in range(0, len(outputValues)):
        if sorted(outputValues[i]) in inputValuesSorted:
            index = inputValuesSorted.index(sorted(outputValues[i]))
            resultat.append(inputDigits[index])

    return resultat

def main(fichier):

    lines = fileManipulation.read_file_line_by_line(fichier)

    total = 0

    for l in lines:
        outputDigits = ""
        for c in get_output_digits(l):
            outputDigits += str(c)
        total += int(outputDigits)

    return total

if __name__ == "__main__":
       print(main('input.txt'))
