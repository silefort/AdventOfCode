import tools.fileManipulation as fileManipulation

def test_read_file_line_by_line_ligne_1_est_bien_lue():
    # Given
    filename = "input.txt"

    # When
    resultat = fileManipulation.read_file_line_by_line(filename)

    # Then
    assert resultat[0].strip() == "Ligne 1"

def test_read_file_line_by_line_ligne_2_est_bien_lue():
    # Given
    filename = "input.txt"

    # When
    resultat = fileManipulation.read_file_line_by_line(filename)

    # Then
    assert resultat[1].strip() == "Ligne 2"

def test_read_file_line_by_line_nombre_de_lignes_est_correct():
    # Given
    filename = "input.txt"

    # When
    resultat = fileManipulation.read_file_line_by_line(filename)

    # Then
    assert len(resultat) == 4

def test_read_file_line_by_line_fichier_entier_est_lu():
    # Given
    filename = "input.txt"

    # When
    resultat = fileManipulation.read_file_line_by_line(filename)

    # Then
    assert resultat == ['Ligne 1', 'Ligne 2', 'Ligne 3', 'Ligne 4']

def test_read_file_line_by_line_to_int_fichier_entier_est_lu():
    # Given
    filename = "input_int.txt"

    # When
    resultat = fileManipulation.read_file_line_by_line_to_int(filename)

    # Then
    assert resultat == [1,2,3,4]

def test_read_file_col_by_col():
    # Given
    filename = "input_col.txt"

    # When
    resultat = fileManipulation.read_file_col_by_col(filename)

    # Then
    assert resultat == ['011110011100', '010001010101', '111111110000', '011101100011', '000111100100']
