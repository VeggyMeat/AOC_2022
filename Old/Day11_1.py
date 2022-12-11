import utils

file = open("Day11.txt", 'r')
data = file.read()
file.close()

paragraphs = utils.paragraphs(data)

items = []
operations = [("*", 13), ("+", 3), ("^", 2), ("+", 5), ("+", 7), ("+", 4), ("*", 19), ("+", 2)]
tests = [5, 7, 13, 11, 3, 2, 17, 19]
results = [(1, 6), (5, 3), (0, 6), (5, 7), (2, 0), (4, 7), (1, 3), (2, 4)]
inspects = [0 for x in range(8)]

for paragraph in paragraphs:
    lines = paragraph.split('\n')
    items.append([int(x) for x in lines[1].split(', ')])

for x in range(20):
    for monkey in range(len(paragraphs)):
        for item in items[monkey]:
            if operations[monkey][0] == "*":
                item *= operations[monkey][1]
            elif operations[monkey][0] == "+":
                item += operations[monkey][1]
            else:
                item *= item
            item //= 3

            if item % tests[monkey] == 0:
                items[results[monkey][0]].append(item)
            else:
                items[results[monkey][1]].append(item)
            inspects[monkey] += 1

        items[monkey] = []

inspects.sort()
print(inspects[-1]*inspects[-2])
