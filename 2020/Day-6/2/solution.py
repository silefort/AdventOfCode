import itertools

def number_of_unique_answers(group):
    return len(list(sort_uniq(list(group.strip().replace('\n','')))))

def number_of_yes(group):
    print(group)
    groupSize = len(group.strip().split('\n'))
    total = 0
    print("groupSize= " + str(groupSize))
    for l in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        if group.count(l) == groupSize:
            total += 1
    print("total= " + str(total))
    return total

def sort_uniq(sequence):
        return (x[0] for x in itertools.groupby(sorted(sequence)))

def main(filename):
    file1 = open(filename, 'r')
    myList = file1.read().split('\n\n')

    total = 0
    for group in myList:
        total += number_of_yes(group)
    file1.close()

    return total

if __name__ == '__main__':
    solution = main('input')
    print(solution)
