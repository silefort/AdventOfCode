import sys 
sys.path.append('..')
import tools.fileManipulation as fileManipulation

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
    if nombreDe1 > (len(colonne) - nombreDe1):
        return '1'
    else:
        return '0'

def main(fichier):

    
    colonnes = fileManipulation.read_file_col_by_col(fichier)
    gammaRate = calcul_gamma_rate(colonnes)
    epsilonRate = calcul_epsilon_rate(gammaRate)

    return int(gammaRate,2) * int(epsilonRate,2)

if __name__ == "__main__":
       print(main('input.txt'))
