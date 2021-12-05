from main import *

def test_main():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = main(fichier)

    # Then
    assert resultat == 1924

def test_get_draw_numbers_list():
    # Given
    fichier = 'test_input.txt'
    lines = fileManipulation.read_file_line_by_line(fichier)

    # When
    resultat = get_draw_numbers_list(lines)

    # Then
    assert resultat == [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

def test_create_grid():
    # Given
    fichier = 'test_input.txt'
    lines = fileManipulation.read_file_line_by_line(fichier)
    inputGrid = lines[2:7]

    # When
    resultat = create_grid(inputGrid)

    # Then
    assert resultat == [[(22,0), (13,0), (17,0), (11,0),  (0,0)],
                        [ (8,0),  (2,0), (23,0),  (4,0), (24,0)],
                        [(21,0),  (9,0), (14,0), (16,0),  (7,0)],
                        [ (6,0), (10,0),  (3,0), (18,0),  (5,0)],
                        [ (1,0), (12,0), (20,0), (15,0), (19,0)]]

def test_extract_grids():
    # Given
    fichier = 'test_input.txt'
    lines = fileManipulation.read_file_line_by_line(fichier)
    inputGrid = lines[2:]

    # When
    resultat = extract_grids(inputGrid)

    # Then
    assert len(resultat) == 3

def test_extract_input():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = extract_input(fichier)

    # Then
    assert resultat[0] == [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    assert len(resultat[1]) == 3

def test_is_number_in_grid():
    # Given
    number = 23
    grid = [[(22,0), (13,0), (17,0), (11,0),  (0,0)],
            [ (8,0),  (2,0), (23,0),  (4,0), (24,0)],
            [(21,0),  (9,0), (14,0), (16,0),  (7,0)],
            [ (6,0), (10,0),  (3,0), (18,0),  (5,0)],
            [ (1,0), (12,0), (20,0), (15,0), (19,0)]]

    # When
    resultat = is_number_in_grid(grid, number)

    # Then
    assert resultat == [(2,1)]

def test_is_line_full_True():
    #Given
    grid = [[(22,0), (13,0), (17,0), (11,0),  (0,0)],
            [ (8,0),  (2,1), (23,0),  (4,0), (24,0)],
            [(21,1),  (9,1), (14,1), (16,1),  (7,1)],
            [ (6,0), (10,0),  (3,1), (18,1),  (5,0)],
            [ (1,0), (12,0), (20,0), (15,1), (19,0)]]

    # When
    resultat = is_line_full(grid)

    # Then
    assert resultat == True

def test_is_line_full_False():
    #Given
    grid = [[(22,0), (13,0), (17,0), (11,0),  (0,0)],
            [ (8,0),  (2,0), (23,0),  (4,0), (24,0)],
            [(21,1),  (9,0), (14,1), (16,1),  (7,1)],
            [ (6,0), (10,0),  (3,0), (18,0),  (5,0)],
            [ (1,0), (12,0), (20,0), (15,0), (19,0)]]

    # When
    resultat = is_line_full(grid)

    # Then
    assert resultat == False

def test_is_colonne_full_True():
    #Given
    grid = [[(22,0), (13,1), (17,0), (11,0),  (0,0)],
            [ (8,0),  (2,1), (23,0),  (4,0), (24,0)],
            [(21,0),  (9,1), (14,1), (16,1),  (7,1)],
            [ (6,0), (10,1),  (3,0), (18,0),  (5,0)],
            [ (1,0), (12,1), (20,0), (15,0), (19,0)]]

    # When
    resultat = is_colonne_full(grid)

    # Then
    assert resultat == True

def test_is_colonne_full_False():
    #Given
    grid = [[(22,0), (13,0), (17,0), (11,0),  (0,0)],
            [ (8,0),  (2,0), (23,0),  (4,0), (24,0)],
            [(21,1),  (9,0), (14,1), (16,1),  (7,1)],
            [ (6,0), (10,0),  (3,0), (18,0),  (5,0)],
            [ (1,0), (12,0), (20,0), (15,0), (19,0)]]

    # When
    resultat = is_colonne_full(grid)

    # Then
    assert resultat == False

def test_update_grid():
    #Given
    grid = [[(22,0), (13,0), (17,0), (11,0),  (0,0)],
            [ (8,0),  (2,0), (23,0),  (4,0), (24,0)],
            [(21,1),  (9,0), (14,1), (16,1),  (7,1)],
            [ (6,0), (10,0),  (3,0), (18,0),  (5,0)],
            [ (1,0), (12,0), (20,0), (15,0), (19,0)]]
    number = 1

    # When
    outputGrid = update_grid(grid, number)

    # Then
    assert outputGrid == [[(22,0), (13,0), (17,0), (11,0),  (0,0)],
                    [ (8,0),  (2,0), (23,0),  (4,0), (24,0)],
                    [(21,1),  (9,0), (14,1), (16,1),  (7,1)],
                    [ (6,0), (10,0),  (3,0), (18,0),  (5,0)],
                    [ (1,1), (12,0), (20,0), (15,0), (19,0)]]

def test_is_game_finished_false():
    #Given
    grids = [[[(22,0), (13,0), (17,0), (11,0),  (0,0)],
            [ (8,0),  (2,0), (23,0),  (4,0), (24,0)],
            [(21,1),  (9,0), (14,1), (16,1),  (7,1)],
            [ (6,0), (10,0),  (3,0), (18,0),  (5,0)],
            [ (1,0), (12,0), (20,0), (15,0), (19,0)]]]
    fullBoards = []

    # When
    gameFinished = is_game_finished(grids,fullBoards)

    # Then
    assert gameFinished == []

def test_is_game_finished_true():
    #Given
    grids = [[[(22,0), (13,0), (17,0), (11,0),  (0,0)],
            [ (8,0),  (2,0), (23,0),  (4,0), (24,0)],
            [(21,1),  (9,1), (14,1), (16,1),  (7,0)],
            [ (6,0), (10,0),  (3,0), (18,0),  (5,0)],
            [ (1,0), (12,0), (20,0), (15,0), (19,0)]],
            [[(22,0), (13,0), (17,0), (11,0),  (0,0)],
            [ (8,0),  (2,0), (23,0),  (4,0), (24,0)],
            [(21,1),  (9,1), (14,1), (16,1),  (7,1)],
            [ (6,0), (10,0),  (3,0), (18,0),  (5,0)],
            [ (1,0), (12,0), (20,0), (15,0), (19,0)]]]

    fullBoards = []

    # When
    gameFinished = is_game_finished(grids,fullBoards)

    # Then
    assert gameFinished == [1]

def test_sum_of_unmarked():
    #Given
    grid = [[(22,0), (13,0), (17,0), (11,0),  (0,0)],
            [ (8,0),  (2,0), (23,0),  (4,0), (24,0)],
            [(21,1),  (9,1), (14,1), (16,1),  (7,1)],
            [ (6,0), (10,0),  (3,0), (18,0),  (5,0)],
            [ (1,0), (12,0), (20,0), (15,0), (19,0)]]

    # When
    sumUnmarked = sum_of_unmarked(grid)

    # Then
    assert sumUnmarked == 233

def test_find_grid_to_win_last():
    #Given
    grids = [[[(22,0), (13,0), (17,0), (11,0),  (0,0)],
            [ (8,0),  (2,0), (23,0),  (4,0), (24,0)],
            [(21,1),  (9,1), (14,1), (16,1),  (7,0)],
            [ (6,0), (10,0),  (3,0), (18,0),  (5,0)],
            [ (1,0), (12,0), (20,0), (15,0), (19,0)]],
            [[(22,0), (13,0), (17,0), (11,0),  (0,0)],
            [ (8,0),  (2,0), (23,0),  (4,0), (24,0)],
            [(21,1),  (9,1), (14,1), (16,1),  (7,1)],
            [ (6,0), (10,0),  (3,0), (18,0),  (5,0)],
            [ (1,0), (12,0), (20,0), (15,0), (19,0)]]]

    # When
    lastWinningGrid = find_grid_to_win_last(grids)

    # Then
    assert lastWinningGrid == 1
