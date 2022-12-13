import utils
import json

file = open("Day13.txt", 'r')
data = file.read()
file.close()

lines = [line for line in data.split('\n') if line != ""]
lines.append("[[2]]")
lines.append("[[6]]")

stringT = type(1)
listT = type([])
total = 0


def compareTwo(a, b):
    if type(a) == stringT:
        if type(b) == stringT:
            if a > b:
                return False
            elif a < b:
                return 2
        if type(b) == listT:
            a = [a]

    if type(a) == listT:
        if type(b) == stringT:
            b = [b]

        for x in range(len(a)):
            if x >= len(b):
                return False

            out = compareTwo(a[x], b[x])
            if not out:
                return False
            elif out == 2:
                return 2

        if len(a) < len(b):
            return 2
    return True


cleanLines = []
for line in lines:
    cleanLines.append(json.loads(line))

sortedLines = [0 for x in range(len(cleanLines))]

for n, line1 in enumerate(cleanLines):
    smaller = 0
    for x, line2 in enumerate(cleanLines):
        if x != n:
            if not compareTwo(line1, line2):
                smaller += 1
    sortedLines[smaller] = line1

print((sortedLines.index([[6]]) + 1) * (sortedLines.index([[2]]) + 1))
