import utils

file = open("Day10.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')
cycle = 0
totalX = 1
out = 0
output = ""
for line in lines:
    if line == 'noop':
        if totalX + 1 >= cycle % 40 >= totalX - 1:
            output += '#'
        else:
            output += '.'
        cycle += 1
    else:
        if totalX + 1 >= cycle % 40 >= totalX - 1:
            output += '#'
        else:
            output += '.'
        cycle += 1
        if totalX + 1 >= cycle % 40 >= totalX - 1:
            output += '#'
        else:
            output += '.'
        cycle += 1
        totalX += int(line.split(' ')[1])

for x in range(6):
    print(output[40*x:40*x+40])