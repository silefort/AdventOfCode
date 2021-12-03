import sys 
sys.path.append('..')
import tools.fileManipulation as fileManipulation

def main(fichier):

    nombreDeMeasurementIncrease = 0
    measurements = fileManipulation.read_file_line_by_line_to_int(fichier)
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            nombreDeMeasurementIncrease += 1

    return nombreDeMeasurementIncrease

if __name__ == "__main__":
       print(main('input.txt'))
