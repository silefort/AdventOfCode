import sys 
sys.path.append('..')
import tools.fileManipulation as fileManipulation

def compute_cells_to_update(vent):
    updateList = []
    if is_vert_line(vent):
        minRange = min(vent[0][0],(vent[1][0]))
        maxRange = max(vent[0][0],(vent[1][0]))
        for i in range(minRange, maxRange+1):
            updateList.append((i,vent[1][1]))
    if is_horiz_line(vent):
        minRange = min(vent[0][1],(vent[1][1]))
        maxRange = max(vent[0][1],(vent[1][1]))
        for i in range(minRange, maxRange+1):
            updateList.append((vent[1][0],i))
    return updateList

def string_to_vent(strVent):
    source = (int(strVent.split(' -> ')[0].split(',')[0]),int(strVent.split(' -> ')[0].split(',')[1]))
    destination = (int(strVent.split(' -> ')[1].split(',')[0]),int(strVent.split(' -> ')[1].split(',')[1]))
    return (source, destination)

def is_vert_line(vent):
    return vent[0][1] == vent[1][1]

def is_horiz_line(vent):
    return vent[0][0] == vent[1][0]

def get_vents(filename):

    lines = fileManipulation.read_file_line_by_line(filename)
    vents = []
    for l in lines:
        vents.append(string_to_vent(l))

    return vents

def get_max_x(vents):

    xList = []
    for v in vents:
        xList.append(v[0][0])
        xList.append(v[1][0])

    return max(xList)

def get_max_y(vents):

    yList = []
    for v in vents:
        yList.append(v[0][1])
        yList.append(v[1][1])

    return max(yList)

def update_matrix(vents, matrix):

    currentMatrix = matrix
    for v in vents:
        cellsToUpdate = compute_cells_to_update(v)
        for c in cellsToUpdate:
            y = c[0]
            x = c[1]
            currentMatrix[x][y] = currentMatrix[x][y] + 1

    return currentMatrix

def main(fichier):


    vents = get_vents(fichier)
    rows = get_max_x(vents) + 1
    columns = get_max_y(vents) + 1
    matrix = []
    for r in range(0,rows):
        currentRow = []
        for c in range(0,columns):
            currentRow.append(0)
        matrix.append(currentRow)

    matrix = update_matrix(vents,matrix)

    numberOfDangerousAreas = 0
    for r in range(0,rows):
        for c in range(0, columns):
            if matrix[r][c] >= 2:
                numberOfDangerousAreas += 1

    return numberOfDangerousAreas

if __name__ == "__main__":
       print(main('input.txt'))
