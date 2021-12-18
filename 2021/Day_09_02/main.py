import sys 
sys.path.append('..')
import tools.fileManipulation as fileManipulation

def create_map(fichier):

    lineFile = fileManipulation.read_file_line_by_line(fichier)
    outputMap = []
    for l in lineFile:
        currentLine = []
        for c in l:
            currentLine.append(int(c))
        outputMap.append(currentLine)

    return outputMap

def is_lowest(currentMap, x, y):
    return currentMap[y][x] < min(get_adjacent_values(currentMap, x, y))

def get_lowest_points(currentMap):
    
    lowestPointsList = []
    for y in range(0, len(currentMap)):
        for x in range(0, len(currentMap[0])):
            if is_lowest(currentMap, x, y):
                lowestPointsList.append((x,y))

    return lowestPointsList

def get_adjacent_values(currentMap, x, y):
    adjacentValues = []
    if x:
        adjacentValues.append(currentMap[y][x-1])
    if y:
        adjacentValues.append(currentMap[y-1][x])
    if x < len(currentMap[0])-1:
        adjacentValues.append(currentMap[y][x+1])
    if y < len(currentMap)-1:
        adjacentValues.append(currentMap[y+1][x])

    return adjacentValues

def explore(currentMap, x, y):
    adjacentPos = []
    if x and currentMap[y][x-1] != 9 and currentMap[y][x-1] != -1:
        adjacentPos.append((x-1,y))
    if y and currentMap[y-1][x] != 9 and currentMap[y-1][x] != -1:
        adjacentPos.append((x,y-1))
    if x < len(currentMap[0])-1 and currentMap[y][x+1] != 9 and currentMap[y][x+1] != -1:
        adjacentPos.append((x+1,y))
    if y < len(currentMap)-1 and currentMap[y+1][x] != 9  and currentMap[y+1][x] != -1:
        adjacentPos.append((x,y+1))

    return adjacentPos

def main(fichier):

    currentMap = create_map(fichier)
    lowestPointsList = get_lowest_points(currentMap)

    # listToExplore = [lowestPointsList[0]]
    listToExplore = [(6,4)]
    bassinSizes = []

    for b in lowestPointsList:

        bassinSize = 0
        listToExplore = [b]
        while len(listToExplore):
            nextExplorationList = []
            for p in listToExplore:
                bassinSize += 1
                nextExplorationList += explore(currentMap, p[0], p[1])
                currentMap[p[1]][p[0]] = -1
            listToExplore = []
            for i in nextExplorationList:
                if i not in listToExplore:
                    listToExplore.append(i)
        bassinSizes.append(bassinSize)

    return sorted(bassinSizes, reverse=True)[0] * sorted(bassinSizes, reverse=True)[1] * sorted(bassinSizes, reverse=True)[2]

if __name__ == "__main__":
       print(main('input.txt'))
