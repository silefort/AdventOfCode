import sys 
sys.path.append('..')
import tools.fileManipulation as fileManipulation

def forward(instruction, horizontalPosition, depthPosition):
    return (horizontalPosition + instruction, depthPosition)

def up(instruction, horizontalPosition, depthPosition):
    return (horizontalPosition, depthPosition - instruction)

def down(instruction, horizontalPosition, depthPosition):
    return (horizontalPosition, depthPosition + instruction)

def lit_instruction(instruction):
    return (instruction.split(' ')[0], int(instruction.split(' ')[1]))

def calcul_position(ligneInstruction, horizontalPosition, depthPosition):
    instruction = lit_instruction(ligneInstruction)
    direction = instruction[0]
    distance = instruction[1]
    position =(0,0)
    if direction == "forward":
        position = forward(distance, horizontalPosition, depthPosition)
    elif direction == "up":
        position = up(distance, horizontalPosition, depthPosition)
    elif direction == "down":
        position = down(distance, horizontalPosition, depthPosition)

    return position

def main(fichier):

    instructions = fileManipulation.read_file_line_by_line(fichier)
    position = (0,0)
    for i in instructions:
        position = calcul_position(i, position[0], position[1])

    return position[0] * position[1]

if __name__ == "__main__":
       print(main('input.txt'))
