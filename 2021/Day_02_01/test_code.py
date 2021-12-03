from main import *

def test_main():
    # Given
    fichier = 'test_input.txt'

    # When
    resultat = main(fichier)

    # Then
    assert resultat == 150

def test_forward():
    # Given
    forwardInstruction = 5
    horizontalPosition = 0
    depthPosition = 0

    # When
    nouvellePosition = forward(forwardInstruction, horizontalPosition, depthPosition)

    # Then
    assert nouvellePosition == (5,0)

def test_up():
    # Given
    upInstruction = 3
    horizontalPosition = 0
    depthPosition = 5

    # When
    nouvellePosition = up(upInstruction, horizontalPosition, depthPosition)

    # Then
    assert nouvellePosition == (0,2)

def test_down():
    # Given
    downInstruction = 3
    horizontalPosition = 0
    depthPosition = 5

    # When
    nouvellePosition = down(downInstruction, horizontalPosition, depthPosition)

    # Then
    assert nouvellePosition == (0,8)

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
    position = (0,0)

    # When
    position = calcul_position(ligneInstruction, position[0], position[1])

    # Then
    assert position == (5,0)
