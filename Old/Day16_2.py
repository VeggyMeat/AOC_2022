import utils

# file = open("Day16.txt", 'r')
file = open("Day16T.txt", 'r')
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

    shortest = [1 for _ in range(60)]
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

non_zero_S = set(non_zero)

for y, valve1 in enumerate(non_zero):
    for x, valve2 in enumerate(non_zero):
        if y != x:
            N_Paths[(valve1, valve2)] = len(find_shortest_path(valve1, valve2, []))
            been = {}


best = [0]


def search(open, n_node, e_node, n=0, pressure=0, et=0, nt=0, ep='', np=''):
    pressure_c = sum([pressures[x] for x in open])
    if set(open) == non_zero_S:
        return pressure + pressure_c * (27 - n)

    n_options = []
    if nt == 0:
        if np != '':
            n_node = np
            open.append(np)
            np = ''
        for valve in non_zero:
            if valve != n_node:
                if valve not in open:
                    number = N_Paths[valve, n_node] + 1
                    n_options.append([valve, number])

    e_options = []
    if et == 0:
        if ep != '':
            e_node = ep
            open.append(ep)
            ep = ''
        for valve in non_zero:
            if valve != e_node:
                if valve not in open:
                    number = N_Paths[valve, e_node] + 1
                    e_options.append([valve, number])

    backs = []
    if et <= 0 and nt <= 0:
        for option1 in n_options:
            for option2 in e_options:
                if option1[0] != option2[0]:
                    if option1[0] not in open and option2[0] not in open:
                        gap = min(option2[1], option1[1])
                        gap = max(gap, 1)
                        if n + gap > 26:
                            backs.append(pressure + pressure_c * (27 - n))
                        else:
                            backs.append(search(open[:], n_node, e_node, n + gap, pressure + pressure_c * gap, option2[1] - gap, option1[1] - gap, option2[0], option1[0]))
    elif et == 0:
        for option2 in e_options:
            if option2[0] != np:
                if option2[0] not in open:
                    gap = min(option2[1], nt)
                    gap = max(gap, 1)
                    if n + gap > 26:
                        backs.append(pressure + pressure_c * (27 - n))
                    else:
                        backs.append(search(open[:], n_node, e_node, n + gap, pressure + pressure_c * gap, option2[1] - gap, nt - gap, option2[0], np))
    elif nt == 0:
        for option1 in n_options:
            if option1[0] != ep:
                if option1[0] not in open:
                    gap = min(et, option1[1])
                    gap = max(gap, 1)
                    if n + gap > 26:
                        backs.append(pressure + pressure_c * (27 - n))
                    else:
                        backs.append(search(open[:], n_node, e_node, n + gap, pressure + pressure_c * gap, et - gap, option1[1] - gap, ep, option1[0]))
    else:
        gap = min(et, nt)
        gap = max(gap, 1)
        if n + gap > 26:
            return pressure + pressure_c * (27 - n)
        else:
            return search(open[:], n_node, e_node, n + gap, pressure + pressure_c * gap, et - gap, nt - gap, ep, np)

    if len(backs) > 0:
        return max(backs)
    else:
        gap = min(et, nt)
        gap = max(gap, 1)
        if n + gap > 26:
            return pressure + pressure_c * (27 - n)
        else:
            return search(open[:], n_node, e_node, n + gap, pressure + pressure_c * gap, et - gap, nt - gap, ep, np)


print(search(['AA'], 'AA', 'AA'))
