from main import *

def test_compte_depth_measurements():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = main(fichier)

    # Then
    assert resultat == 7
