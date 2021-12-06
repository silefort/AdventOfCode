import sys 
sys.path.append('..')
import tools.fileManipulation as fileManipulation

def update_lanternfish(lanternFish):
    lanternFishOutput = []
    if lanternFish > 0:
        lanternFishOutput.append(lanternFish-1)
    else:
        lanternFishOutput.append(6)
        lanternFishOutput.append(8)

    return lanternFishOutput

def update_lanternfish_list(lanternFishList):

    lanternFishListOutput = []
    for i in lanternFishList:
        lanternFishOutput = update_lanternfish(i)
        for l in lanternFishOutput:
            lanternFishListOutput.append(l)

    return lanternFishListOutput

def main(fichier):

    lanternFishLine = fileManipulation.read_file_line_by_line(fichier)[0]
    lanternFishList = []
    for l in lanternFishLine.split(','):
        lanternFishList.append(int(l))

    for i in range(0,80):
        lanternFishList = update_lanternfish_list(lanternFishList)

    return len(lanternFishList)

if __name__ == "__main__":
       print(main('input.txt'))
