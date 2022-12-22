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

for command in commands:
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

            while grid[new_pos[1]][new_pos[0]] == ' ':
                if heading == 0:
                    new_pos = (new_pos[0] + 1, new_pos[1])
                elif heading == 1:
                    new_pos = (new_pos[0], new_pos[1] + 1)
                elif heading == 2:
                    new_pos = (new_pos[0] - 1, new_pos[1])
                else:
                    new_pos = (new_pos[0], new_pos[1] - 1)

                new_pos = (new_pos[0] % max_width, new_pos[1] % max_height)

            if grid[new_pos[1]][new_pos[0]] == '#':
                break
            else:
                pos = new_pos

print(1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + heading)