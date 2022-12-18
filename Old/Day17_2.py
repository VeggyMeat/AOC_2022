import utils

file = open("Day17.txt", 'r')
data = file.read()
file.close()

height_size = 200000

rocks = [['.' for _ in range(7)] for x in range(height_size)]
rocks.append([])

height_above = 4
max_height = height_size


def rock_fall(rock):
    new_rock = []
    for point in rock:
        new_rock.append((point[0], point[1] + 1))

    for point in new_rock:
        if point[1] <= height_size - 1:
            if rocks[point[1]][point[0]] != '.':
                return False
        else:
            return False
    return new_rock


def rock_wind(rock, d):
    if d == '<':
        new_rock = []
        for point in rock:
            new_rock.append((point[0] - 1, point[1]))
    else:
        new_rock = []
        for point in rock:
            new_rock.append((point[0] + 1, point[1]))

    for point in new_rock:
        if 0 <= point[0] <= 6:
            if rocks[point[1]][point[0]] != '.':
                return rock
        else:
            return rock
    return new_rock


wind = data
# wind = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
rock_patterns = [[(2, 0), (3, 0), (4, 0), (5, 0)], [(3, 0), (3, -1), (2, -1), (4, -1), (3, -2)], [(3, 0), (2, 0), (4, 0), (4, -1), (4, -2)], [(2, -3), (2, -2), (2, -1), (2, 0)], [(3, -1), (2, -1), (2, 0), (3, 0)]]
total_count = 0
# top row, wind count, rock
past = []
for count in range(805):
    rock = rock_patterns[count % 5]
    new_rock = []

    for point in rock:
        new_rock.append((point[0], max_height + point[1] - height_above))

    rock = new_rock
    while True:
        wind_current = wind[total_count]
        rock = rock_wind(rock, wind_current)

        total_count += 1
        total_count = total_count % len(wind)

        out = rock_fall(rock)
        if not out:
            break
        rock = out

    for point in rock:
        rocks[point[1]][point[0]] = '#'
        if point[1] < max_height:
            max_height = point[1]

    for item in past:
        if item[0] == rocks[max_height]:
            if item[2] % 5 == count % 5:
                if total_count == item[1]:
                    print(item)
                    print((rocks[max_height][:], total_count, count, max_height))
                    break
    past.append((rocks[max_height][:], total_count, count, max_height))
print(total_count)
print(height_size - max_height)
