import sys 
sys.path.append('..')
import tools.fileManipulation as fileManipulation

def fuel_spent(source, dest):
    fuelSpent = 0
    for i in range(1, abs(dest-source)+1):
        fuelSpent += i

    return fuelSpent

def list_crabs(crabsList):

    maxPos = max(crabsList)+1
    crabsListOutput = [0 for i in range(maxPos)]
    for i in range(0, maxPos):
        crabsListOutput[i] = crabsList.count(i)

    return crabsListOutput

def compute_total_fuel(crabsList,position):

    totalFuel = 0
    for i in range(0,len(crabsList)):
        # totalFuel += (abs(i-position) * crabsList[i])
        totalFuel += (fuel_spent(i,position) * crabsList[i])

    return totalFuel

def find_best_position(crabsList):

    bestPosition = 0
    bestTotalFuel = -1
    for i in range(0,len(crabsList)):
        print(str(i) + "/" + str(len(crabsList)))
        totalFuel = compute_total_fuel(crabsList, i)
        if bestTotalFuel == -1:
            bestTotalFuel = totalFuel
        elif totalFuel < bestTotalFuel:
            bestTotalFuel = totalFuel
            bestPosition = i

    return bestPosition

def main(fichier):

    crabsListStr = fileManipulation.read_file_line_by_line(fichier)[0].split(',')
    crabsListInt = []
    for i in crabsListStr:
        crabsListInt.append(int(i))

    crabsListPosition = list_crabs(crabsListInt)
    crabsListBestPosition = find_best_position(crabsListPosition)
    crabsTotalFuel = compute_total_fuel(crabsListPosition,crabsListBestPosition)

    return crabsTotalFuel

if __name__ == "__main__":
       print(main('input.txt'))
