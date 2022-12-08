import utils

file = open("Day8.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

visible = []
for y, line in enumerate(lines):
    greatest = -1
    for x, num in enumerate(line):
        if int(num) > greatest:
            greatest = int(num)
            if [x, y] not in visible:
                visible.append([x, y])

for y, line in enumerate(lines):
    greatest = -1
    for x in range(len(lines[0]) - 1, -1, -1):
        num = lines[y][x]
        if int(num) > greatest:
            greatest = int(num)
            if [x, y] not in visible:
                visible.append([x, y])

for x in range(len(lines[0])):
    greatest = -1
    for y in range(len(lines)):
        if int(lines[y][x]) > greatest:
            greatest = int(lines[y][x])
            if [x, y] not in visible:
                visible.append([x, y])

for x in range(len(lines[0])):
    greatest = -1
    for y in range(len(lines) - 1, -1, -1):
        if int(lines[y][x]) > greatest:
            greatest = int(lines[y][x])
            if [x, y] not in visible:
                visible.append([x, y])

print(len(visible))