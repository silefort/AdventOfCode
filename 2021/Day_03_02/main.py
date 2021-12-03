import sys 
sys.path.append('..')
import tools.fileManipulation as fileManipulation

def line_to_col(lignes):
    nbCol = len(lignes[0])

    colonnes = []
    for i in range(0,nbCol):
        strCol = ""
        for j in lignes:
            strCol += j[i]
        colonnes.append(strCol)

    return colonnes

def calcul_oxygen_generator_rating(fichier):

    lignes = fileManipulation.read_file_line_by_line(fichier)
    colonneCourante = 0

    while len(lignes) > 1:
       colonnes = line_to_col(lignes)
       bitCommun = plus_commun_bit(colonnes[colonneCourante]) 
       lignes = calcul_filtre_numbers(lignes, bitCommun, colonneCourante)
       colonneCourante += 1

    return lignes[0]

def calcul_CO2_scrubber_rating(fichier):

    lignes = fileManipulation.read_file_line_by_line(fichier)
    colonneCourante = 0

    while len(lignes) > 1:
       colonnes = line_to_col(lignes)
       bitCommun = str(abs(int(plus_commun_bit(colonnes[colonneCourante])) -1))
       lignes = calcul_filtre_numbers(lignes, bitCommun, colonneCourante)
       colonneCourante += 1

    return lignes[0]

def calcul_filtre_numbers(lignes, filtre, colonne):
    lignesFiltrees = []
    for ligne in lignes:
        if ligne[colonne] == filtre:
            lignesFiltrees.append(ligne)

    return lignesFiltrees

def calcul_gamma_rate(colonnes):
    gammaRate = ""
    for c in colonnes:
        gammaRate += plus_commun_bit(c)
        
    return gammaRate

def calcul_epsilon_rate(gammaRate):
    epsilonRate = ''
    for l in gammaRate:
        epsilonRate += str(abs(int(l)-1))
    return epsilonRate

def plus_commun_bit(colonne):
    nombreDe1 = colonne.count('1') 
    if nombreDe1 >= (len(colonne) - nombreDe1):
        return '1'
    else:
        return '0'

def main(fichier):

    oxygenGeneratorRating = calcul_oxygen_generator_rating(fichier)
    CO2ScrubberRating = calcul_CO2_scrubber_rating(fichier)

    return int(oxygenGeneratorRating,2) * int(CO2ScrubberRating,2)

if __name__ == "__main__":
       print(main('input.txt'))
