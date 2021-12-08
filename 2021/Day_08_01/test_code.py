from main import *

def test_main():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = main(fichier)

    # Then
    assert resultat == 26

def test_get_output_values():
    # Given
    line = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"

    # When
    resultat = get_output_values(line)

    # Then
    assert resultat == ['fdgacbe', 'cefdb', 'cefbgd',  'gcbe']

def test_get_output_values_sizes():
    # Given
    line = ['fdgacbe', 'cefdb', 'cefbgd',  'gcbe']

    # When
    resultat = get_output_values_sizes(line)

    # Then
    assert resultat == [7, 5, 6, 4]

def test_get_all_values_sizes():
    # Given
    fichier = 'test_input.txt'
    lines = fileManipulation.read_file_line_by_line(fichier)[0:2]

    # When
    resultat = get_all_values_sizes(lines)

    # Then
    assert resultat == [7, 5, 6, 4, 6, 3, 7, 2]
