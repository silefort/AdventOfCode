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

    res = 1
    myMoves = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    for l in myMoves:
        res =  res * get_nb_tree(myList,l[0],l[1])

    return res
        
        
if __name__ == '__main__':
    solution = main('input')
    print(solution)
