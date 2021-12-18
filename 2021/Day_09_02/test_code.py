from main import *

def test_main():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = main(fichier)

    # Then
    assert resultat == 1134

def test_create_map():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = create_map(fichier)

    # Then
    assert resultat == [[2,1,9,9,9,4,3,2,1,0],
                        [3,9,8,7,8,9,4,9,2,1],
                        [9,8,5,6,7,8,9,8,9,2],
                        [8,7,6,7,8,9,6,7,8,9],
                        [9,8,9,9,9,6,5,6,7,8]]

def test_is_lowest_point_00():
    # Given
    currentMap = [[2,1,9,9,9,4,3,2,1,0],
                  [3,9,8,7,8,9,4,9,2,1],
                  [9,8,5,6,7,8,9,8,9,2],
                  [8,7,6,7,8,9,6,7,8,9],
                  [9,8,9,9,9,6,5,6,7,8]]

    # When
    resultat = is_lowest(currentMap, 0, 0)

    # Then
    assert resultat == False

def test_is_lowest_point_10():
    # Given
    currentMap = [[2,1,9,9,9,4,3,2,1,0],
                  [3,9,8,7,8,9,4,9,2,1],
                  [9,8,5,6,7,8,9,8,9,2],
                  [8,7,6,7,8,9,6,7,8,9],
                  [9,8,9,9,9,6,5,6,7,8]]

    # When
    resultat = is_lowest(currentMap, 1, 0)

    # Then
    assert resultat == True

def test_get_lowest_points():
    # Given
    currentMap = [[2,1,9,9,9,4,3,2,1,0],
                  [3,9,8,7,8,9,4,9,2,1],
                  [9,8,5,6,7,8,9,8,9,2],
                  [8,7,6,7,8,9,6,7,8,9],
                  [9,8,9,9,9,6,5,6,7,8]]

    # When
    resultat = get_lowest_points(currentMap)

    # Then
    assert resultat == [(1,0),(9,0),(2,2),(6,4)]

def test_get_adjacent_00():
    # Given
    currentMap = [[2,1,9,9,9,4,3,2,1,0],
                  [3,9,8,7,8,9,4,9,2,1],
                  [9,8,5,6,7,8,9,8,9,2],
                  [8,7,6,7,8,9,6,7,8,9],
                  [9,8,9,9,9,6,5,6,7,8]]

    # When
    resultat = get_adjacent_values(currentMap, 0, 0)

    # Then
    assert resultat == [1,3]

def test_explore_00():
    # Given
    currentMap = [[2,1,9,9,9,4,3,2,1,0],
                  [3,9,8,7,8,9,4,9,2,1],
                  [9,8,5,6,7,8,9,8,9,2],
                  [8,7,6,7,8,9,6,7,8,9],
                  [9,8,9,9,9,6,5,6,7,8]]

    # When
    resultat = explore(currentMap, 0, 0)

    # Then
    assert resultat == [(1,0),(0,1)]

def test_explore_10():
    # Given
    currentMap = [[2,1,9,9,9,4,3,2,1,0],
                  [3,9,8,7,8,9,4,9,2,1],
                  [9,8,5,6,7,8,9,8,9,2],
                  [8,7,6,7,8,9,6,7,8,9],
                  [9,8,9,9,9,6,5,6,7,8]]

    # When
    resultat = explore(currentMap, 1, 0)

    # Then
    assert resultat == [(0,0)]
