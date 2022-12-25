import utils

file = open("Day24.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

height = len(lines)
width = len(lines[0])

start = (1, 0)
end = (100, 36)
# end = (6, 5)

blizzards = []
blizzards_winds = []

for y, row in enumerate(lines):
    for x, tile in enumerate(row):
        if tile == 'v':
            blizzards.append((x, y))
            blizzards_winds.append((0, 1))
        elif tile == '<':
            blizzards.append((x, y))
            blizzards_winds.append((-1, 0))
        elif tile == '^':
            blizzards.append((x, y))
            blizzards_winds.append((0, -1))
        elif tile == '>':
            blizzards.append((x, y))
            blizzards_winds.append((1, 0))


def sim_blizzards(blizzards):
    new_blizzards = []
    for n, blizzard in enumerate(blizzards):
        new_blizzards.append(((blizzard[0] + blizzards_winds[n][0] - 1) % (width - 2) + 1, (blizzard[1] + blizzards_winds[n][1] - 1) % (height - 2) + 1))
    return new_blizzards


search = [start, 0]
next_search = set()
deep = 0
next_blizzards = sim_blizzards(blizzards)
while True:
    item = search.pop(0)
    if item == end:
        break
    elif item == 0:
        deep += 1
        blizzards = next_blizzards[:]
        next_blizzards = sim_blizzards(blizzards)
        next_search = set()
        search.append(0)
    else:
        if (item[0] + 1, item[1]) not in next_blizzards and width - 1 > item[0] + 1 and item[1] > 0:
            if (item[0] + 1, item[1]) not in next_search:
                search.append((item[0] + 1, item[1]))
                next_search.add((item[0] + 1, item[1]))
        if (item[0] - 1, item[1]) not in next_blizzards and item[0] - 1 > 0 and item[1] > 0:
            if (item[0] - 1, item[1]) not in next_search:
                search.append((item[0] - 1, item[1]))
                next_search.add((item[0] - 1, item[1]))
        if (item[0], item[1] + 1) not in next_blizzards and (height - 1 > item[1] + 1 or (item[0], item[1] + 1) == end):
            if (item[0], item[1] + 1) not in next_search:
                search.append((item[0], item[1] + 1))
                next_search.add((item[0], item[1] + 1))
        if (item[0], item[1] - 1) not in next_blizzards and item[1] - 1 > 0:
            if (item[0], item[1] - 1) not in next_search:
                search.append((item[0], item[1] - 1))
                next_search.add((item[0], item[1] - 1))
        if item not in next_blizzards:
            if item not in next_search:
                search.append(item)
                next_search.add(item)

print(deep)
