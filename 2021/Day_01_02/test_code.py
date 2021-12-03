from main import *

def test_compte_depth_measurements():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = main(fichier)

    # Then
    assert resultat == 5

def test_somme_3_measurements():
    # Given
    measurements = [1,2,3]

    # When
    somme = somme_3_measurements(measurements)

    # Then
    assert somme == 6

