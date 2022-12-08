import utils

file = open("Day8.txt", 'r')
data = file.read()
file.close()


lines = data.split('\n')

visible = []
highest_scenic_score = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        num = int(lines[y][x])
        final = 1
        count = 0
        for x_change in range(1, len(lines[0])-x):
            if int(lines[y][x+x_change]) < num:
                count += 1
            else:
                count += 1
                break
        final *= count
        count = 0
        for x_change in range(-1, -x-1, -1):
            if int(lines[y][x+x_change]) < num:
                count += 1
            else:
                count += 1
                break
        final *= count
        count = 0
        for y_change in range(1, len(lines)-y):
            if int(lines[y+y_change][x]) < num:
                count += 1
            else:
                count += 1
                break
        final *= count
        count = 0
        for y_change in range(-1, -y-1, -1):
            if int(lines[y + y_change][x]) < num:
                count += 1
            else:
                count += 1
                break
        final *= count

        if final > highest_scenic_score:
            highest_scenic_score = final

print(highest_scenic_score)
