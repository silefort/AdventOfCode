import sys 
sys.path.append('..')
import tools.fileManipulation as fileManipulation

def get_output_values(line):
    return (line.split('| ')[1]).split(' ')

def get_output_values_sizes(line):
    sizes = []
    for l in line:
        sizes.append(len(l))

    return sizes

def get_all_values_sizes(lines):
    allSizes = []
    for l in lines:
        outputValues = get_output_values(l)
        allSizes = allSizes + get_output_values_sizes(outputValues)

    return allSizes

def main(fichier):

    lines = fileManipulation.read_file_line_by_line(fichier)
    allSizes = get_all_values_sizes(lines)

    return allSizes.count(2) + allSizes.count(3) + allSizes.count(4) + allSizes.count(7)

if __name__ == "__main__":
       print(main('input.txt'))
