from main import *

def test_list_crabs():
    # Given
    crabsList = [16,1,2,0,4,2,7,1,2,14]

    # When
    resultat = list_crabs(crabsList)

    # Then
    assert resultat == [1,2,3,0,1,0,0,1,0,0,0,0,0,0,1,0,1]

def test_find_best_position():
    # Given
    crabsList = [1,2,3,0,1,0,0,1,0,0,0,0,0,0,1,0,1]

    # When
    resultat = find_best_position(crabsList)

    # Then
    assert resultat == 2

def test_compute_total_distance():
    # Given
    crabsList = [1,2,3,0,1,0,0,1,0,0,0,0,0,0,1,0,1]
    position = 2

    # When
    resultat = compute_total_distance(crabsList, position)

    # Then
    assert resultat == 37


def test_main():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = main(fichier)

    # Then
    assert resultat == 37
