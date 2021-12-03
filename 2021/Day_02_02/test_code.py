from main import *

def test_main():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = main(fichier)

    # Then
    assert resultat == 900

def test_forward():
    # Given
    forwardInstruction = 5
    horizontalPosition = 0
    depthPosition = 0
    aim = 3

    # When
    nouvellePosition = forward(forwardInstruction, horizontalPosition, depthPosition,aim)

    # Then
    assert nouvellePosition == (5,15,3)

def test_up():
    # Given
    upInstruction = 3
    horizontalPosition = 0
    depthPosition = 5
    aim = 5

    # When
    nouvellePosition = up(upInstruction, horizontalPosition, depthPosition,aim)

    # Then
    assert nouvellePosition == (0,5,2)

def test_down():
    # Given
    downInstruction = 3
    horizontalPosition = 2
    depthPosition = 1
    aim = 3

    # When
    nouvellePosition = down(downInstruction, horizontalPosition, depthPosition, aim)

    # Then
    assert nouvellePosition == (2,1,6)

def test_lit_instruction():
    # Given
    ligneInstruction = "forward 5"

    # When
    instruction = lit_instruction(ligneInstruction)

    # Then
    assert instruction == ("forward", 5)

def test_calcul_position():
    # Given
    ligneInstruction = "forward 5"
    position = (0,0,0)

    # When
    position = calcul_position(ligneInstruction, position[0], position[1], position[2])

    # Then
    assert position == (5,0,0)
