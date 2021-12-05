import sys 
sys.path.append('..')
import tools.fileManipulation as fileManipulation

def sum_of_unmarked(grid):
    sumUnmarked = 0
    for l in grid:
        for m in l:
            if m[1] == 0:
                sumUnmarked += m[0]
    return sumUnmarked

def is_game_finished(grids):
    gameFinished = -1
    for i in range(0, len(grids)):
        if is_line_full(grids[i]) or is_colonne_full(grids[i]):
            gameFinished = i
    return gameFinished

def update_grid(grid, number):
    numberInGrid = is_number_in_grid(grid, number)
    outputGrid = grid
    if numberInGrid != []:
        for position in numberInGrid:
            outputGrid[position[1]][position[0]] = (number, 1)

    return outputGrid

def is_line_full(grid):

    output = False
    for l in grid:
        sumLine = 0
        for m in l:
            sumLine += m[1]
        if sumLine == len(l):
            output = True

    return output

def is_colonne_full(grid):

    output = False
    for i in range(0, len(grid)):
        sumLine = 0
        for j in range(0, len(grid[0])):
            sumLine += grid[j][i][1]
        if sumLine == len(grid):
            output = True

    return output

def is_number_in_grid(grid, number):

    output = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j][0] == number:
                output.append((j,i))
				
    return output

def extract_input(fichier):

    lines = fileManipulation.read_file_line_by_line(fichier)
    drawNumbersList = get_draw_numbers_list(lines)
    grids = extract_grids(lines[2:])

    return (drawNumbersList, grids)

def extract_grids(inputGrid):

    i = 0
    grids = []
    while i < (len(inputGrid) - 1):
        currentGrid = inputGrid[i:i+5]
        currentOutputGrid = create_grid(currentGrid)
        grids.append(currentOutputGrid)
        i+=6

    return grids

def create_grid(inputGrid):

    outputGrid = []
    for l in inputGrid:
        currentOutput = []
        currentLine = l.split()
        for m in currentLine:
            currentOutput.append((int(m),0))
        outputGrid.append(currentOutput)

    return outputGrid

def get_draw_numbers_list(lines):
    return [int(i) for i in lines[0].split(',')]

def main(fichier):

    (numberDrawList, grids) = extract_input(fichier)
    gameFinished = -1
    numberId = 0
    while gameFinished < 0:
        currentNumber = numberDrawList[numberId]
        for i in range(0, len(grids)):
            grids[i] = update_grid(grids[i], currentNumber)
        gameFinished = is_game_finished(grids)
        numberId += 1

    return sum_of_unmarked(grids[gameFinished]) * numberDrawList[numberId -1]

if __name__ == "__main__":
       print(main('input.txt'))
