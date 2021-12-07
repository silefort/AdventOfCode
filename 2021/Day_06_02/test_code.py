from main import *

def test_update_lanternfish_5():
    # Given
    lanternFish = 5

    # When
    resultat = update_lanternfish(lanternFish)

    # Then
    assert resultat == [4]

def test_update_lanternfish_0():
    # Given
    lanternFish = 0

    # When
    resultat = update_lanternfish(lanternFish)

    # Then
    assert resultat == [6,8]

def test_update_lanternfish_list_34():
    # Given
    lanternFishList = [0,0,0,1,1,0,0,0,0]

    # When
    resultat = update_lanternfish_list(lanternFishList)

    # Then
    assert resultat == [0,0,1,1,0,0,0,0,0]

def test_update_lanternfish_list_34312():
    # Given
    lanternFishList = [0,1,1,2,1,0,0,0,0]

    # When
    resultat = update_lanternfish_list(lanternFishList)

    # Then
    assert resultat == [1,1,2,1,0,0,0,0,0]

def test_update_lanternfish_list_23201():
    # Given
    lanternFishList = [1,1,2,1,0,0,0,0,0]

    # When
    resultat = update_lanternfish_list(lanternFishList)

    # Then
    assert resultat == [1,2,1,0,0,0,1,0,1]

def test_convert_lantern_fish_list():
    # Given
    lanternFishList = [3,4,3,1,2]

    # When
    resultat = convert_lantern_fish_list(lanternFishList)

    # Then
    assert resultat == [0,1,1,2,1,0,0,0,0]

def test_main():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = main(fichier)

    # Then
    assert resultat == 26984457539
