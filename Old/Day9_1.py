import utils

file = open("Day9.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

translation = {(2, 2): (1, 1), (2, 1): (1, 1), (2, 0): (1, 0), (2, -1): (1, -1), (2, -2): (1, -1), (1, -2): (1, -1), (0, -2): (0, -1), (-1, -2): (-1, -1), (-2, -2): (-1, -1), (-2, -1): (-1, -1), (-2, 0): (-1, 0), (-2, 1): (-1, 1), (-2, 2): (-1, 1), (-1, 2): (-1, 1), (0, 2): (0, 1), (1, 2): (1, 1)}

chain = [(0, 0), (0, 0)]

past_pos = [(0, 0)]

for line in lines:
    spaces = line.split(' ')
    command = spaces[0]
    for x in range(int(spaces[1])):
        if command == "U": chain[0] = (chain[0][0], chain[0][1] - 1)
        elif command == "D": chain[0] = (chain[0][0], chain[0][1] + 1)
        elif command == "L": chain[0] = (chain[0][0] - 1, chain[0][1])
        elif command == "R": chain[0] = (chain[0][0] + 1, chain[0][1])

        dx = chain[0][0] - chain[1][0]
        dy = chain[0][1] - chain[1][1]

        if (dx, dy) in translation:
            move = translation[(dx, dy)]

            chain[1] = (chain[1][0] + move[0], chain[1][1] + move[1])

            if chain[1] not in past_pos:
                past_pos.append(chain[1])

print(len(past_pos))
