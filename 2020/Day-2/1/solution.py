def is_password_legit(minValue, maxValue, letter, password):
    return count_iteration(letter,password) >= minValue and count_iteration(letter, password) <= maxValue

def count_iteration(letter,password):
    return password.count(letter)

def main(filename):
    total = 0
    file1 = open(filename, 'r')
    myList = file1.readlines() 
    for line in myList:
        minMax = line.split(' ')[0]
        minValue = int(minMax.split('-')[0])
        maxValue = int(minMax.split('-')[1])

        letter = line.split(' ')[1].split(':')[0]
        password = line.split(' ')[2]

        if is_password_legit(minValue, maxValue, letter, password):
            total += 1

    file1.close()
    return total

if __name__ == '__main__':
    solution = main('input')
    print(solution)
