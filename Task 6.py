import re

def light(instructionType, startCoordinate, endCoordinate, field):
    
    if(instructionType == "toggle"):
        for r in range(startCoordinate[0], endCoordinate[0]+1):
            for c in range(startCoordinate[1], endCoordinate[1]+1):
                field[r][c] = field[r][c]+2
                
    elif(instructionType == "turn off"):
        for r in range(startCoordinate[0], endCoordinate[0]+1):
            for c in range(startCoordinate[1], endCoordinate[1]+1):
                field[r][c] -= 1
                if(field[r][c] < 0):
                    field[r][c] = 0
    elif(instructionType == "turn on"):
        for r in range(startCoordinate[0], endCoordinate[0]+1):
            for c in range(startCoordinate[1], endCoordinate[1]+1):
                field[r][c] += 1
                

file = open("input6.txt")

instructions = file.read().split("\n")
# s1 = "turn off 370,39 through 425,839"
# m = re.search(r"\d", s1)
# if m:
#     print("Digit found at position", m.start())
rows, cols = 1000,1000
field = [[0 for j in range(cols)] for i in range(rows)]
for instruction in instructions:
    m = re.search(r"\d", instruction)
    instructionType = ""
    if m:
        instructionType = instruction[0:m.start()-1]
        instruction = instruction[m.start():]
    startCoordinate = instruction[:instruction.index(" ")].split(",")
    instruction = instruction[instruction.index(" "):]
    m = re.search(r"\d", instruction)
    endCoordinate = []
    if m:
        endCoordinate = instruction[m.start():].split(",")
    sc = [int(startCoordinate[0]), int(startCoordinate[1])]
    ec = [int(endCoordinate[0]), int(endCoordinate[1])]
    light(instructionType, sc, ec, field)

lightUp = 0
for l in field:
    lightUp += sum(l)

print(lightUp)