import utils

file = open("Day7.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

dir = []
tree = {}

for line in lines:
    spaces = line.split(' ')
    if spaces[0] == '$':
        if spaces[1] == 'cd':
            if spaces[2] == '..':
                dir.pop()
            else:
                dir.append(spaces[2])
    else:
        if ' '.join(dir) not in tree:
            tree[' '.join(dir)] = [0, []]
        if spaces[0] != 'dir':
            tree[' '.join(dir)][0] += int(spaces[0])
        else:
            tree[' '.join(dir)][1].append(spaces[1])


def count(dir):
    total = tree[dir][0]
    for dir1 in tree[dir][1]:
        total += count(dir + ' ' + dir1)
    return total


totals = []
for directory in tree:
    totals.append(count(directory))
totals.sort()

unused = 70000000 - count('/')
for size in totals:
    if size > 30000000 - unused:
        print(size)
        break