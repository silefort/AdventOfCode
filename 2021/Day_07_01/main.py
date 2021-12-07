import sys 
sys.path.append('..')
import tools.fileManipulation as fileManipulation

def list_crabs(crabsList):

    maxPos = max(crabsList)+1
    crabsListOutput = [0 for i in range(maxPos)]
    for i in range(0, maxPos):
        crabsListOutput[i] = crabsList.count(i)

    return crabsListOutput

def compute_total_distance(crabsList,position):

    totalDistance = 0
    for i in range(0,len(crabsList)):
        totalDistance += (abs(i-position) * crabsList[i])

    return totalDistance

def find_best_position(crabsList):

    bestPosition = 0
    bestTotalDistance = -1
    for i in range(0,len(crabsList)):
        totalDistance = compute_total_distance(crabsList, i)
        if bestTotalDistance == -1:
            bestTotalDistance = totalDistance
        elif totalDistance < bestTotalDistance:
            bestTotalDistance = totalDistance
            bestPosition = i

    return bestPosition

def main(fichier):

    crabsListStr = fileManipulation.read_file_line_by_line(fichier)[0].split(',')
    crabsListInt = []
    for i in crabsListStr:
        crabsListInt.append(int(i))

    crabsListPosition = list_crabs(crabsListInt)
    crabsListBestPosition = find_best_position(crabsListPosition)
    crabsTotalDistance = compute_total_distance(crabsListPosition,crabsListBestPosition)

    return crabsTotalDistance

if __name__ == "__main__":
       print(main('input.txt'))
