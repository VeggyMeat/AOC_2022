import utils

file = open("Day18.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

points = set()
orthoganol = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
total = 0


for line in lines:
    points.add(tuple([int(x) for x in line.split(',')]))

for point in points:
    for side in orthoganol:
        new = (point[0] + side[0], point[1] + side[1], point[2] + side[2])
        if new not in points:
            total += 1

print(total)
