import utils
import time

file = open("Day12.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

# lines = ["Sbc", "fed", "ghE"]

grid = [[0 for x in range(len(lines[0]))] for y in range(len(lines))]
places = [(1, 0), (-1, 0), (0, 1), (0, -1)]

to = (0, 0)
current = (0, 0)

alph = "abcdefghijklmnopqrstuvwxyz"
char_to_num = {alph[x]: x + 1 for x in range(26)}

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "S":
            grid[y][x] = 1
            to = (x, y)
        elif char == "E":
            grid[y][x] = 26
            current = (x, y)
        else:
            grid[y][x] = char_to_num[char]

places_been = {(x, y): 999 for x in range(len(lines[0])) for y in range(len(lines))}


def search(spot, spot_to, moves):
    if moves > 900:
        return 999

    if places_been[spot] <= moves:
        return 999
    else:
        places_been[spot] = moves

    if spot[0] == spot_to[0] and spot[1] == spot_to[1]:
        return moves

    char_current = grid[spot[1]][spot[0]]
    best = []

    for place in places:
        spot_place = (spot[0] + place[0], spot[1] + place[1])
        if 0 <= spot_place[0] <= len(lines[0]) - 1 and 0 <= spot_place[1] <= len(lines) - 1:
            if char_current - 1 <= grid[spot_place[1]][spot_place[0]]:
                best.append(search(spot_place, spot_to, moves + 1))

    if len(best) == 0:
        return 999

    return min(best)

things = []
N = time.time()
for x in range(0, len(lines)):
    things.append(search(current, (0, x), 0))
    places_been = {(x, y): 999 for x in range(len(lines[0])) for y in range(len(lines))}
    print(x)
print(min(things))
print(time.time() - N)
