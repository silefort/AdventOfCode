import sys 
sys.path.append('..')
import tools.fileManipulation as fileManipulation

def return_adjacent(matrix,x,y):

    output = []
    if y:
        output.append(matrix[y-1][x])
    if x:
        output.append(matrix[y][x-1])
    if x < (len(matrix[0])-1):
        output.append(matrix[y][x+1])
    if y < (len(matrix)-1):
        output.append(matrix[y+1][x])
    
    return output

def is_lowest(matrix,x,y):

    return matrix[y][x] < min(return_adjacent(matrix,x,y))

def main(fichier):

    matrix = fileManipulation.read_file_line_by_line(fichier)

    sumLowest = 0

    for x in range(0, len(matrix[0])):
        for y in range(0, len(matrix)):
            if is_lowest(matrix, x, y):
                # print("x=" + str(x) + " y=" + str(y) + " xy=" + str(matrix[y][x]))
                # print(return_adjacent(matrix, x, y))
                sumLowest += (int(matrix[y][x])+1)

    return sumLowest

if __name__ == "__main__":
       print(main('input.txt'))
