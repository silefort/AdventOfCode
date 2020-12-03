def get_case(line, position):
    return line[position%(len(line.strip()))]

def get_nb_tree(myList, right, down):
    position = 0
    nbTrees = 0

    count = 0
    for line in myList:
        if count % down == 0:
            if get_case(line,position) == '#':
                nbTrees += 1
            position += right
        count +=1
    
    return nbTrees
    
def main(filename):
    file1 = open(filename, 'r')
    myList = file1.readlines()
    file1.close()

    return get_nb_tree(myList,3,1)
        
if __name__ == '__main__':
    solution = main('input')
    print(solution)
