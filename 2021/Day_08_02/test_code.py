from main import *

def test_main():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = main(fichier)

    # Then
    assert resultat == 61229

def test_get_output_values():
    # Given
    line = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"

    # When
    resultat = get_output_values(line)

    # Then
    assert resultat == ['fdgacbe', 'cefdb', 'cefbgd',  'gcbe']

def test_get_input_values():
    # Given
    line = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"

    # When
    resultat = get_input_values(line)

    # Then
    assert resultat == ['be','cfbegad',  'cbdgef',  'fgaecd',  'cgeb',  'fdcge',  'agebfd',  'fecdb',  'fabcd',  'edb']

def test_find_7():
    # Given
    line = ['be','cfbegad',  'cbdgef',  'fgaecd',  'cgeb',  'fdcge',  'agebfd',  'fecdb',  'fabcd',  'edb']

    # When
    resultat = find_7(line)

    # Then
    assert resultat == 9

def test_find_1():
    # Given
    line = ['be','cfbegad',  'cbdgef',  'fgaecd',  'cgeb',  'fdcge',  'agebfd',  'fecdb',  'fabcd',  'edb']

    # When
    resultat = find_1(line)

    # Then
    assert resultat == 0

def test_find_4():
    # Given
    line = ['be','cfbegad',  'cbdgef',  'fgaecd',  'cgeb',  'fdcge',  'agebfd',  'fecdb',  'fabcd',  'edb']

    # When
    resultat = find_4(line)

    # Then
    assert resultat == 4

def test_find_8():
    # Given
    line = ['be','cfbegad',  'cbdgef',  'fgaecd',  'cgeb',  'fdcge',  'agebfd',  'fecdb',  'fabcd',  'edb']

    # When
    resultat = find_8(line)

    # Then
    assert resultat == 1

def test_find_5():
    # Given
    line = ['be','cfbegad',  'cbdgef',  'fgaecd',  'cgeb',  'fdcge',  'agebfd',  'fecdb',  'fabcd',  'edb']

    # When
    resultat = find_5(line)

    # Then
    assert resultat == 5

def test_find_3():
    # Given
    line = ['be','cfbegad',  'cbdgef',  'fgaecd',  'cgeb',  'fdcge',  'agebfd',  'fecdb',  'fabcd',  'edb']

    # When
    resultat = find_3(line)

    # Then
    assert resultat == 7

def test_find_2():
    # Given
    line = ['be','cfbegad',  'cbdgef',  'fgaecd',  'cgeb',  'fdcge',  'agebfd',  'fecdb',  'fabcd',  'edb']

    # When
    resultat = find_2(line)

    # Then
    assert resultat == 8

def test_find_6():
    # Given
    line = ['be','cfbegad',  'cbdgef',  'fgaecd',  'cgeb',  'fdcge',  'agebfd',  'fecdb',  'fabcd',  'edb']

    # When
    resultat = find_6(line)

    # Then
    assert resultat == 3

def test_find_0():
    # Given
    line = ['be','cfbegad',  'cbdgef',  'fgaecd',  'cgeb',  'fdcge',  'agebfd',  'fecdb',  'fabcd',  'edb']

    # When
    resultat = find_0(line)

    # Then
    assert resultat == 6

def test_find_9():
    # Given
    line = ['be','cfbegad',  'cbdgef',  'fgaecd',  'cgeb',  'fdcge',  'agebfd',  'fecdb',  'fabcd',  'edb']

    # When
    resultat = find_9(line)

    # Then
    assert resultat == 2

def test_substract():
    # Given
    val1 = ['b','e']
    val2 = ['b','e', 'c', 'g']

    # When
    resultat = substract(val1, val2)

    # Then
    assert resultat == ['c', 'g']

def test_find_values():
    # Given
    line = ['be','cfbegad',  'cbdgef',  'fgaecd',  'cgeb',  'fdcge',  'agebfd',  'fecdb',  'fabcd',  'edb']

    # When
    resultat = find_values(line)

    # Then
    assert resultat == [1, 8, 9, 6, 4, 5, 0, 3, 2, 7]

def test_get_output_digits():
    # Given
    line = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"

    # When
    resultat = get_output_digits(line)

    # Then
    assert resultat == [8, 3, 9, 4]
