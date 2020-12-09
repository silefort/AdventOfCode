def split_line(line):
    # Clean line:
    for w in [' bags', ' bag', '.']:
        line = line.replace(w,'')

    # topBag
    topBag = line.split(' contain ')[0].strip()
    listBags = line.split(' contain ')[1].strip().split(', ')
    print(topBag)
    print(listBags)

def main(filename):
    file1 = open(filename, 'r')
    myList = file1.readlines()
    containers = ['shiny gold']
    keep = True
    while keep:
        current = 0
        for l in myList:
            for c in containers:
                container = l.split(' bags contain ')[0]
                if c in l.split(' contain ')[1] and container not in containers:
                    containers.append(l.split(' bags contain ')[0])
                    print(containers)
                    current += 1
        if current == 0:
            keep = False

    return len(containers)-1

if __name__ == '__main__':
    solution = main('input')
    print(solution)
