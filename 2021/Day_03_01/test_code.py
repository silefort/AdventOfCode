from main import *

def test_main():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = main(fichier)

    # Then
    assert resultat == 198

def test_plus_commun_bit():
    # Given
    colonne = '01111'

    # When
    resultat = plus_commun_bit(colonne)

    # Then
    assert resultat == '1'

def test_plus_commun_bit_2():
    # Given
    colonne = '01000'

    # When
    resultat = plus_commun_bit(colonne)

    # Then
    assert resultat == '0'

def test_calcul_gamma_rate():
    # Given
    fichier = 'input.txt'
    colonnes = fileManipulation.read_file_col_by_col(fichier)

    # When
    resultat = calcul_gamma_rate(colonnes)

    # Then
    assert resultat == '10110'

def test_calcul_epsilon_rate():

    # Given
    gammaRate = '10110'

    # When
    epsilonRate = calcul_epsilon_rate(gammaRate)

    # Then
    assert epsilonRate == '01001'
