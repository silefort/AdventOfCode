import itertools

def split_line(line):
    # Clean line:
    for w in [' bags', ' bag', '.']:
        line = line.replace(w,'')

    # topBag
    topBag = line.split(' contain ')[0].strip()
    listBags = []
    for b in line.split(' contain ')[1].strip().split(', '):
        currentBag = b.split(' ',1)
        if currentBag[0] != "no":
            listBags.append((int(currentBag[0]),currentBag[1]))
    return (topBag, listBags)

def get_number_bags(myLines, color):
    total = 0
    for l in myLines:
        if color == split_line(l)[0]:
            print("myline= ", split_line(l))
            for b in split_line(l)[1]:
                print('\t' + str(get_number_bags(myLines, b[1])))
                total = total +  b[0] + (b[0] * get_number_bags(myLines, b[1]))
    return total

def main(filename):
    file1 = open(filename, 'r')
    myList = file1.readlines()
    file1.close()
    return get_number_bags(myList,"shiny gold")

if __name__ == '__main__':
    solution = main('input')
    print(solution)
