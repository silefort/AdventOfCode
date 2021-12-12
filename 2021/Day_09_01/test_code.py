from main import *

def test_main():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = main(fichier)

    # Then
    assert resultat == 15

def test_is_lowest_00():
    # Given
    fichier = 'test_input.txt'
    matrix = fileManipulation.read_file_line_by_line(fichier)

    # When
    resultat = is_lowest(matrix,0,0)

    # Then
    assert resultat == False

def test_is_lowest_01():
    # Given
    fichier = 'test_input.txt'
    matrix = fileManipulation.read_file_line_by_line(fichier)

    # When
    resultat = is_lowest(matrix,1,0)

    # Then
    assert resultat == True

def test_return_adjacent_11():
    # Given
    matrix = [[2,1,9,9],
              [3,9,8,7],
              [9,8,5,6]]

    # When
    resultat = return_adjacent(matrix,1,1)

    # Then
    assert resultat == [1,3,8,8]

def test_return_adjacent_01():
    # Given
    matrix = [[2,1,9,9],
              [3,9,8,7],
              [9,8,5,6]]

    # When
    resultat = return_adjacent(matrix,1,0)

    # Then
    assert resultat == [2,9,9]

def test_return_adjacent_00():
    # Given
    matrix = [[2,1,9,9],
              [3,9,8,7],
              [9,8,5,6]]

    # When
    resultat = return_adjacent(matrix,0,0)

    # Then
    assert resultat == [1,3]

def test_return_adjacent_32():
    # Given
    matrix = [[2,1,9,9],
              [3,9,8,7],
              [9,8,5,6]]

    # When
    resultat = return_adjacent(matrix,3,2)

    # Then
    assert resultat == [7,5]

def test_return_adjacent_22():
    # Given
    matrix = [[2,1,9],
              [3,9,8],
              [9,8,5]]

    # When
    resultat = return_adjacent(matrix,2,2)

    # Then
    assert resultat == [8,8]

def test_return_adjacent_12():
    # Given
    matrix = [[2,1,9],
              [3,9,8],
              [9,8,5]]

    # When
    resultat = return_adjacent(matrix,1,2)

    # Then
    assert resultat == [9,9,5]
