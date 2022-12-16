import utils

file = open("Day16.txt", 'r')
# file = open("Day16T.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

paths = {}
pressures = {}

for line in lines:
    parts = line.split('; ')
    valve = parts[0][6:8]
    flow_rate = int(parts[0][23:])

    valves_out = parts[1].split(' ')[4:]
    for n, x in enumerate(valves_out):
        if n != len(valves_out) - 1:
            valves_out[n] = x[:2]
    pressures[valve] = flow_rate
    paths[valve] = valves_out

print(paths)
print(pressures)

prev = {}

been = {}


def find_shortest_path(valve1, valve2, d):
    pathss = []
    if valve1 == valve2:
        return d

    if valve1 in been:
        if been[valve1] < len(d):
            return False

    been[valve1] = len(d)

    for valve in paths[valve1]:
        c = d[:]
        c.append(valve)
        pathss.append(find_shortest_path(valve, valve2, c))

    shortest = [1 for x in range(60)]
    for path in pathss:
        if path:
            if len(path) < len(shortest):
                shortest = path[:]

    return shortest


# only want paths inbetween non 0 valves

non_zero = ['AA']
N_Paths = {}

for valve in pressures:
    if pressures[valve] != 0:
        non_zero.append(valve)

for y, valve1 in enumerate(non_zero):
    for x, valve2 in enumerate(non_zero):
        if y != x:
            N_Paths[(valve1, valve2)] = len(find_shortest_path(valve1, valve2, []))
            been = {}

print(N_Paths)


def search(open, n, pressure, node):
    if n > 30:
        return pressure
    pressure_c = sum([pressures[x] for x in open])

    # all moves
    backs = []
    for valve in non_zero:
        if valve != node:
            if valve not in open:
                number = 1 + N_Paths[valve, node]
                if n + number < 30:
                    new = open[:]
                    new.append(valve)
                    backs.append(search(new, n + number, pressure + pressure_c * number, valve))
    if len(backs) == 0:
        return search(open, n + 1, pressure + pressure_c, node)
    return max(backs)


print(search([], 1, 0, 'AA'))
