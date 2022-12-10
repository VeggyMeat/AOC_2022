import utils

file = open("Day10.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')
cycle = 0
totalX = 1
out = 0
for line in lines:
    if line == 'noop':
        cycle += 1
        if cycle % 40 == 20:
            out += totalX * cycle
            print(totalX, cycle)
    else:
        cycle += 1
        if cycle % 40 == 20:
            out += totalX * cycle
            print(totalX, cycle)
        cycle += 1
        if cycle % 40 == 20:
            out += totalX * cycle
            print(totalX, cycle)
        totalX += int(line.split(' ')[1])

print(out)