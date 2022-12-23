import utils
import copy

file = open("Day23.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

data = [list(x) for x in lines]

height = len(data) + 20
width = len(data[0]) + 20

elves = [['.' for _ in range(width)] for _ in range(10)]
for row in data:
    row1 = ['.' for _ in range(10)]
    row1.extend(row)
    row1.extend(['.' for _ in range(10)])
    elves.extend([row1])

elves.extend([['.' for _ in range(width)] for _ in range(10)])

for t in range(10):
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

top_left_bottom_right = (30, 30, 30, 30)

for y, row in enumerate(elves):
    for x, elf in enumerate(row):
        if elf == '#':
            if y < top_left_bottom_right[0]:
                top_left_bottom_right = (y, top_left_bottom_right[1], top_left_bottom_right[2], top_left_bottom_right[3])
            if y > top_left_bottom_right[2]:
                top_left_bottom_right = (top_left_bottom_right[0], top_left_bottom_right[1], y, top_left_bottom_right[3])
            if x < top_left_bottom_right[1]:
                top_left_bottom_right = (top_left_bottom_right[0], x, top_left_bottom_right[2], top_left_bottom_right[3])
            if x > top_left_bottom_right[3]:
                top_left_bottom_right = (top_left_bottom_right[0], top_left_bottom_right[1], top_left_bottom_right[2], x)

count = 0
for y in range(top_left_bottom_right[0], top_left_bottom_right[2] + 1):
    for x in range(top_left_bottom_right[1], top_left_bottom_right[3] + 1):
        if elves[y][x] == '.':
            count += 1

print(count)
