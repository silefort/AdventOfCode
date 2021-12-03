import sys 
sys.path.append('..')
import tools.fileManipulation as fileManipulation

def forward(instruction, horizontalPosition, depthPosition,aim):
    return (horizontalPosition + instruction, depthPosition + aim*instruction, aim)

def up(instruction, horizontalPosition, depthPosition,aim):
    return (horizontalPosition, depthPosition,  aim - instruction)

def down(instruction, horizontalPosition, depthPosition, aim):
    return (horizontalPosition, depthPosition, aim + instruction)

def lit_instruction(instruction):
    return (instruction.split(' ')[0], int(instruction.split(' ')[1]))

def calcul_position(ligneInstruction, horizontalPosition, depthPosition,aim):
    instruction = lit_instruction(ligneInstruction)
    direction = instruction[0]
    distance = instruction[1]
    position =(0,0)
    if direction == "forward":
        position = forward(distance, horizontalPosition, depthPosition,aim)
    elif direction == "up":
        position = up(distance, horizontalPosition, depthPosition,aim)
    elif direction == "down":
        position = down(distance, horizontalPosition, depthPosition,aim)

    return position

def main(fichier):

    instructions = fileManipulation.read_file_line_by_line(fichier)
    position = (0,0,0)
    for i in instructions:
        position = calcul_position(i, position[0], position[1], position[2])

    return position[0] * position[1]

if __name__ == "__main__":
       print(main('input.txt'))
