import utils

file = open("Day18.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

points = set()
orthoganol = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
total = 0
limit = 20


def search(spot):
    done = set()
    queue = [spot]
    while queue:
        item = queue.pop(0)
        for side in orthoganol:
            new = (item[0] + side[0], item[1] + side[1], item[2] + side[2])
            if new not in done:
                if new[0] < 1 or new[0] > 19 or new[1] < 1 or new[1] > 19 or new[2] < 1 or new[2] > 19:
                    return True
                if new not in points:
                    queue.append(new)
                    done.add(new)
    return False


for line in lines:
    points.add(tuple([int(x) for x in line.split(',')]))

bubbles = {}

for point in points:
    print(point)
    for side in orthoganol:
        new = (point[0] + side[0], point[1] + side[1], point[2] + side[2])
        if new not in points:
            if new not in bubbles:
                if search(new):
                    bubbles[new] = True
                    total += 1
                else:
                    bubbles[new] = False
            else:
                if bubbles[new]:
                    total += 1

print(total)
