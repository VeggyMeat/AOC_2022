import utils
import json

file = open("Day13.txt", 'r')
data = file.read()
file.close()

para = data.split('\n\n')

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


for x, lines in enumerate(para):
    strings = []
    for line in lines.split('\n'):
        strings.append(json.loads(line))

    if compareTwo(strings[0], strings[1]):
        total += x + 1

print(total)
