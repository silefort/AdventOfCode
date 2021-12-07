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

    lanternFishListOutput = [0,0,0,0,0,0,0,0,0]
    for i in range(1,9):
        lanternFishListOutput[i-1] = lanternFishList[i]
    lanternFishListOutput[6] = lanternFishListOutput[6] + lanternFishList[0]
    lanternFishListOutput[8] = lanternFishList[0]

    return lanternFishListOutput

def convert_lantern_fish_list(lanternFishList):

    lanternFishListOutput = [0,0,0,0,0,0,0,0,0]
    for i in range(0,8):
        lanternFishListOutput[i] = lanternFishList.count(i)

    return lanternFishListOutput

def main(fichier):

    lanternFishLine = fileManipulation.read_file_line_by_line(fichier)[0]
    lanternFishList = []
    for l in lanternFishLine.split(','):
        lanternFishList.append(int(l))

    lanternFishList = convert_lantern_fish_list(lanternFishList)

    for i in range(0,256):
        lanternFishList = update_lanternfish_list(lanternFishList)

    sumOfFish = 0
    for i in lanternFishList:
        sumOfFish += i

    return sumOfFish

if __name__ == "__main__":
       print(main('input.txt'))
