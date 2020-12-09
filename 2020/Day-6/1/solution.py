import itertools

def number_of_unique_answers(group):
    return len(list(sort_uniq(list(group.strip().replace('\n','')))))

def sort_uniq(sequence):
        return (x[0] for x in itertools.groupby(sorted(sequence)))

def main(filename):
    file1 = open(filename, 'r')
    myList = file1.read().split('\n\n')

    total = 0
    for group in myList:
        total += number_of_unique_answers(group)
    file1.close()

    return total

if __name__ == '__main__':
    solution = main('input')
    print(solution)
