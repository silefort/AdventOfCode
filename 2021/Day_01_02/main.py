import sys 
sys.path.append('..')
import tools.fileManipulation as fileManipulation

def somme_3_measurements(measurements):
    somme = 0
    for i in measurements:
        somme += i
    return somme

def main(fichier):

    nombreDeMeasurementIncrease = 0
    measurements = fileManipulation.read_file_line_by_line_to_int(fichier)
    for i in range(2, len(measurements)-1):
        tripletMeasurementsPrecedent = [measurements[i-2], measurements[i-1], measurements[i]]
        tripletMeasurementsCourant = [measurements[i-1], measurements[i], measurements[i+1]]
        if somme_3_measurements(tripletMeasurementsCourant) > somme_3_measurements(tripletMeasurementsPrecedent):
            nombreDeMeasurementIncrease += 1

    return nombreDeMeasurementIncrease

if __name__ == "__main__":
       print(main('input.txt'))
