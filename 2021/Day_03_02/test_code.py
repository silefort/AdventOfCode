from main import *

def test_main():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = main(fichier)

    # Then
    assert resultat == 230

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

def test_filtre_numbers():
    # Given
    lignes = ['1001','0101','1100','0111']
    filtre = '1'
    colonne = 0

    # When
    resultat = calcul_filtre_numbers(lignes,filtre,colonne)

    # Then
    assert resultat == ['1001', '1100']

def test_filtre_numbers_long():
    # Given
    lignes = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    filtre = '0'
    colonne = 0

    # When
    resultat = calcul_filtre_numbers(lignes,filtre,colonne)

    # Then
    assert resultat == ['00100', '01111', '00111', '00010', '01010']

def test_calcul_gamma_rate():
    # Given
    fichier = 'test_input.txt'
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

def test_calcul_oxygen_generator_rating():
    # Given
    fichier = 'test_input.txt'
    colonnes = fileManipulation.read_file_col_by_col(fichier)

    # When
    oxygenGeneratorRating = calcul_oxygen_generator_rating(fichier)

    # Then
    assert oxygenGeneratorRating == '10111'

def test_calcul_C02_scrubber_rating():
    # Given
    fichier = 'test_input.txt'
    colonnes = fileManipulation.read_file_col_by_col(fichier)

    # When
    CO2ScrubberRating = calcul_CO2_scrubber_rating(fichier)

    # Then
    assert CO2ScrubberRating == '01010'

def test_line_to_col():
    # Given
    lignes = ['1001','0101','1100','0111']

    # When
    colonnes = line_to_col(lignes)

    # Then
    assert colonnes == ['1010', '0111', '0001', '1101']

