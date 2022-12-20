import utils

file = open("Day19.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

blueprints = []

for x, line in enumerate(lines):
    parts = line.split('. ')
    words = [part.split(' ') for part in parts]
    blueprints.append([x + 1, (int(words[0][-2]), 0, 0), (int(words[1][-2]), 0, 0), (int(words[2][-5]), int(words[2][-2]), 0), (int(words[3][-5]), 0, int(words[3][-2]))])


def search(blueprint, items, robots, minutes):
    if minutes == 0:
        return items[3]

    branches = [0]

    for n, robot in enumerate(blueprint):
        if n != 0:
            if items[0] >= robot[0] and items[1] >= robot[1] and items[2] >= robot[2]:
                if items[0] - robots[0] < robot[0] or items[1] - robots[1] < robot[1] or items[2] - robots[2] < robot[2]:
                    new_robots = robots[:]
                    new_robots[n - 1] += 1
                    new_items = [items[0] - robot[0] + robots[0], items[1] - robot[1] + robots[1], items[2] - robot[2] + robots[2], items[3] + robots[3]]
                    branches.append(search(blueprint, new_items, new_robots, minutes - 1))

    items = [item + robots[n] for n, item in enumerate(items)]

    branches.append(search(blueprint, items, robots, minutes - 1))

    return max(branches)


# print(search([1, (4, 0, 0), (2, 0, 0), (3, 14, 0), (2, 0, 7)], [0, 0, 0, 0], [1, 0, 0, 0], 24))

score = 0
for blue in blueprints:
    score += blue[0] * search(blue, [0, 0, 0, 0], [1, 0, 0, 0], 24)

print(score)
