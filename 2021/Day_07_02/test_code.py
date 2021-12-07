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
    assert resultat == 5

def test_fuel_spent_37():
    # Given
    source = 3
    destination = 7

    # When
    resultat = fuel_spent(source, destination)

    # Then
    assert resultat == 10

def test_fuel_spent_165():
    # Given
    source = 16
    destination = 5

    # When
    resultat = fuel_spent(source, destination)

    # Then
    assert resultat == 66

def test_compute_total_fuel():
    # Given
    crabsList = [1,2,3,0,1,0,0,1,0,0,0,0,0,0,1,0,1]
    position = 5

    # When
    resultat = compute_total_fuel(crabsList, position)

    # Then
    assert resultat == 168


def test_main():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = main(fichier)

    # Then
    assert resultat == 168
