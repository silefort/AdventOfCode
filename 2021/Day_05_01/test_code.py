from main import *

def test_update_matrix():
    # Given
    # vents = [((0,9),(5,9)),
            # ((5,5),(8,2))]
    vents = [((0,9),(5,9)),
            ((0,0), (9,9))]

    rows = get_max_x(vents) + 1
    columns = get_max_y(vents) + 1
    matrix = []
    for r in range(0,rows):
        currentRow = []
        for c in range(0,columns):
            currentRow.append(0)
        matrix.append(currentRow)

    # When
    matrix = update_matrix(vents, matrix)

    # Then
    assert matrix ==  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]

def test_main():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = main(fichier)

    # Then
    assert resultat == 5

def test_string_to_vent():
    # Given
    strVent = "0,9 -> 5,9"

    # When
    resultat = string_to_vent(strVent)

    # Then
    assert resultat == ((0,9),(5,9))

def test_get_vents():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = get_vents(fichier)

    # Then
    assert resultat == [((0,9),(5,9)),
                        ((8,0),(0,8)),
                        ((9,4),(3,4)),
                        ((2,2),(2,1)),
                        ((7,0),(7,4)),
                        ((6,4),(2,0)),
                        ((0,9),(2,9)),
                        ((3,4),(1,4)),
                        ((0,0),(8,8)),
                        ((5,5),(8,2))]

def test_get_max_x():
    # Given
    vents = [((0,9),(5,9)),
            ((8,0),(0,8)),
            ((9,4),(3,4)),
            ((2,2),(2,1)),
            ((7,0),(7,4)),
            ((6,4),(2,0)),
            ((0,9),(2,9)),
            ((3,4),(1,4)),
            ((0,0),(8,8)),
            ((5,5),(8,2))]

    # When
    resultat = get_max_x(vents)

    # Then
    assert resultat == 9

def test_get_max_y():
    # Given
    vents = [((0,9),(5,9)),
            ((8,0),(0,8)),
            ((9,4),(3,4)),
            ((2,2),(2,1)),
            ((7,0),(7,4)),
            ((6,4),(2,0)),
            ((0,9),(2,9)),
            ((3,4),(1,4)),
            ((0,0),(8,8)),
            ((5,5),(8,2))]

    # When
    resultat = get_max_x(vents)

    # Then
    assert resultat == 9

def test_is_vert_line():
    # Given
    line =  ((0,9),(5,9))

    # When
    resultat = is_vert_line(line)

    # Then
    assert resultat == True

def test_is_not_vert_line():
    # Given
    line =  ((0,4),(5,9))

    # When
    resultat = is_vert_line(line)

    # Then
    assert resultat == False

def test_is_horiz_line():
    # Given
    line =  ((2,9),(2,4))

    # When
    resultat = is_horiz_line(line)

    # Then
    assert resultat == True

def test_is_not_horiz_line():
    # Given
    line =  ((0,4),(5,9))

    # When
    resultat = is_horiz_line(line)

    # Then
    assert resultat == False

def test_compute_cells_to_update_vert():
    # Given
    line =  ((0,9),(5,9))

    # When
    resultat = compute_cells_to_update(line)

    # Then
    assert resultat == [(0,9),(1,9),(2,9),(3,9),(4,9),(5,9)]

def test_compute_cells_to_update_horiz():
    # Given
    line =  ((4,9),(4,6))

    # When
    resultat = compute_cells_to_update(line)

    # Then
    assert resultat == [(4,6),(4,7),(4,8),(4,9)]
