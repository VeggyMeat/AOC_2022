import utils

file = open("Day22.txt", 'r')
data = file.read()
file.close()

mapp, instructions = data.split('\n\n')

heading = 0

grid = mapp.split('\n')
grid = [list(x) for x in grid]
for row in grid:
    while len(row) < len(grid[0]):
        row.append(' ')

max_width = len(grid[0])
max_height = len(grid)

numbers = instructions.replace('L', ' ')
numbers = numbers.replace('R', ' ')
numbers = numbers.split(' ')
numbers = [int(x) for x in numbers]

directions = instructions
for x in range(10):
    directions = directions.replace(str(x), ' ')

directions = directions.split(' ')
directions = [direction for direction in directions if direction]

pos = (0, 0)
square = (max_width // 3, max_height // 4)
connections = {"00": "321", "01": "220", "03": "530", "12": "401", "13": "500", "20": "030", "22": "410", "30": "021", "31": "520", "42": "101", "43": "200", "50": "330", "51": "010", "52": "110"}
squares = [(2, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3)]


def to_square(pos):
    spot = (pos[0] // square[0], pos[1] // square[1])
    return squares.index(spot)


def to_pos(sqre):
    sqre = squares[sqre]
    return sqre[0] * square[0], sqre[1] * square[1]


for n, x in enumerate(grid[0]):
    if x != ' ':
        pos = (n, 0)
        break

commands = []
for x in range(len(directions) + len(numbers)):
    if x % 2 == 0:
        commands.append(numbers[x // 2])
    if x % 2 == 1:
        commands.append(directions[x // 2])

for n, command in enumerate(commands):
    if command == "R":
        heading += 1
        heading %= 4
    elif command == "L":
        heading -= 1
        heading %= 4
    else:
        for x in range(command):
            if heading == 0:
                new_pos = (pos[0] + 1, pos[1])
            elif heading == 1:
                new_pos = (pos[0], pos[1] + 1)
            elif heading == 2:
                new_pos = (pos[0] - 1, pos[1])
            else:
                new_pos = (pos[0], pos[1] - 1)

            new_pos = (new_pos[0] % max_width, new_pos[1] % max_height)

            new_heading = heading

            if grid[new_pos[1]][new_pos[0]] == ' ':
                spot = to_square(pos)
                code = str(spot) + str(heading)
                out_code = connections[code]
                new_square = int(out_code[0])
                new_heading = int(out_code[1])
                reverse = bool(int(out_code[2]))
                difs = (pos[0] % square[0], pos[1] % square[1])
                new_pos = to_pos(new_square)

                if new_heading == 2:
                    new_pos = (new_pos[0] + square[0] - 1, new_pos[1])
                elif new_heading == 3:
                    new_pos = (new_pos[0], new_pos[1] + square[1] - 1)

                if reverse:
                    if new_heading % 2 == 0:
                        if heading % 2 == 0:
                            new_pos = (new_pos[0], new_pos[1] + square[1] - difs[1] - 1)
                        else:
                            new_pos = (new_pos[0], new_pos[1] + square[1] - difs[0] - 1)
                    else:
                        if heading % 2 == 0:
                            new_pos = (new_pos[0] + square[0] + difs[1] - 1, new_pos[1])
                        else:
                            new_pos = (new_pos[0] + square[0] + difs[0] - 1, new_pos[1])
                else:
                    if new_heading % 2 == 0:
                        if heading % 2 == 0:
                            new_pos = (new_pos[0], new_pos[1] + difs[1])
                        else:
                            new_pos = (new_pos[0], new_pos[1] + difs[0])
                    else:
                        if heading % 2 == 0:
                            new_pos = (new_pos[0] + difs[1], new_pos[1])
                        else:
                            new_pos = (new_pos[0] + difs[0], new_pos[1])

            if grid[new_pos[1]][new_pos[0]] == '#':
                break
            else:
                pos = new_pos
                heading = new_heading

print(1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + heading)