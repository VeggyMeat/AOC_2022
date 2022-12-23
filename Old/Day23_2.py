import utils
import copy

file = open("Day23.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

data = [list(x) for x in lines]

height = len(data) + 500
width = len(data[0]) + 500

elves = [['.' for _ in range(width)] for _ in range(250)]
for row in data:
    row1 = ['.' for _ in range(250)]
    row1.extend(row)
    row1.extend(['.' for _ in range(250)])
    elves.extend([row1])

elves.extend([['.' for _ in range(width)] for _ in range(250)])

for t in range(10000):
    prev_elves = copy.deepcopy(elves)
    num_map = [[0 for _ in range(width)] for _ in range(height)]
    proposed_to = {}
    for y, row in enumerate(elves):
        for x, spot in enumerate(row):
            if spot == '#':
                if elves[y - 1][x - 1] != '.' or elves[y - 1][x] != '.' or elves[y - 1][x + 1] != '.' or elves[y][x + 1] != '.' or elves[y + 1][x + 1] != '.' or elves[y + 1][x] != '.' or elves[y + 1][x - 1] != '.' or elves[y][x - 1] != '.':
                    if t % 4 == 0:
                        if elves[y - 1][x-1] == '.' and elves[y - 1][x] == '.' and elves[y - 1][x+1] == '.':
                            num_map[y - 1][x] += 1
                            proposed_to[(x, y-1)] = (x, y)
                        elif elves[y + 1][x-1] == '.' and elves[y + 1][x] == '.' and elves[y + 1][x+1] == '.':
                            num_map[y + 1][x] += 1
                            proposed_to[(x, y + 1)] = (x, y)
                        elif elves[y - 1][x - 1] == '.' and elves[y][x - 1] == '.' and elves[y + 1][x - 1] == '.':
                            num_map[y][x - 1] += 1
                            proposed_to[(x - 1, y)] = (x, y)
                        elif elves[y - 1][x + 1] == '.' and elves[y][x + 1] == '.' and elves[y + 1][x+1] == '.':
                            num_map[y][x + 1] += 1
                            proposed_to[(x + 1, y)] = (x, y)
                    elif t % 4 == 1:
                        if elves[y + 1][x-1] == '.' and elves[y + 1][x] == '.' and elves[y + 1][x+1] == '.':
                            num_map[y + 1][x] += 1
                            proposed_to[(x, y + 1)] = (x, y)
                        elif elves[y - 1][x - 1] == '.' and elves[y][x - 1] == '.' and elves[y + 1][x - 1] == '.':
                            num_map[y][x - 1] += 1
                            proposed_to[(x - 1, y)] = (x, y)
                        elif elves[y - 1][x + 1] == '.' and elves[y][x + 1] == '.' and elves[y + 1][x+1] == '.':
                            num_map[y][x + 1] += 1
                            proposed_to[(x + 1, y)] = (x, y)
                        elif elves[y - 1][x-1] == '.' and elves[y - 1][x] == '.' and elves[y - 1][x+1] == '.':
                            num_map[y - 1][x] += 1
                            proposed_to[(x, y-1)] = (x, y)
                    elif t % 4 == 2:
                        if elves[y - 1][x - 1] == '.' and elves[y][x - 1] == '.' and elves[y + 1][x - 1] == '.':
                            num_map[y][x - 1] += 1
                            proposed_to[(x - 1, y)] = (x, y)
                        elif elves[y - 1][x + 1] == '.' and elves[y][x + 1] == '.' and elves[y + 1][x+1] == '.':
                            num_map[y][x + 1] += 1
                            proposed_to[(x + 1, y)] = (x, y)
                        elif elves[y - 1][x-1] == '.' and elves[y - 1][x] == '.' and elves[y - 1][x+1] == '.':
                            num_map[y - 1][x] += 1
                            proposed_to[(x, y-1)] = (x, y)
                        elif elves[y + 1][x-1] == '.' and elves[y + 1][x] == '.' and elves[y + 1][x+1] == '.':
                            num_map[y + 1][x] += 1
                            proposed_to[(x, y + 1)] = (x, y)
                    elif t % 4 == 3:
                        if elves[y - 1][x + 1] == '.' and elves[y][x + 1] == '.' and elves[y + 1][x+1] == '.':
                            num_map[y][x + 1] += 1
                            proposed_to[(x + 1, y)] = (x, y)
                        elif elves[y - 1][x-1] == '.' and elves[y - 1][x] == '.' and elves[y - 1][x+1] == '.':
                            num_map[y - 1][x] += 1
                            proposed_to[(x, y-1)] = (x, y)
                        elif elves[y + 1][x-1] == '.' and elves[y + 1][x] == '.' and elves[y + 1][x+1] == '.':
                            num_map[y + 1][x] += 1
                            proposed_to[(x, y + 1)] = (x, y)
                        elif elves[y - 1][x - 1] == '.' and elves[y][x - 1] == '.' and elves[y + 1][x - 1] == '.':
                            num_map[y][x - 1] += 1
                            proposed_to[(x - 1, y)] = (x, y)

    for y, row in enumerate(num_map):
        for x, spot in enumerate(row):
            if spot == 1:
                elf_from = proposed_to[(x, y)]
                elves[elf_from[1]][elf_from[0]] = '.'
                elves[y][x] = '#'

    if elves == prev_elves:
        print(t + 1)
        break
