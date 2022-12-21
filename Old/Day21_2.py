import utils

file = open("Day21.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

dic = {}
links = {}
humn_conncetion = {"humn": True}

lines = [line.split(': ') for line in lines]
original = lines[:]
for line in original:
    if len(line[1].split(' ')) == 1:
        dic[line[0]] = int(line[1])
        lines.remove(line)
        links[line[0]] = False
    else:
        links[line[0]] = line[1].split(' ')

item = "humn"
while True:
    for thing in links:
        if links[thing]:
            if links[thing][0] == item or links[thing][2] == item:
                humn_conncetion[thing] = True
                itemN = thing
                break
    if item == itemN:
        break
    item = itemN

dic.pop("humn")

lines = [[line[0], line[1].split(' ')] for line in lines]

while original != lines:
    original = lines[:]
    for line in original:
        if line[1][0] in dic and line[1][2] in dic:
            if line[1][1] == "+":
                dic[line[0]] = dic[line[1][0]] + dic[line[1][2]]
            elif line[1][1] == "*":
                dic[line[0]] = dic[line[1][0]] * dic[line[1][2]]
            elif line[1][1] == "/":
                dic[line[0]] = dic[line[1][0]] / dic[line[1][2]]
            elif line[1][1] == "-":
                dic[line[0]] = dic[line[1][0]] - dic[line[1][2]]
            lines.remove(line)

for line in lines:
    if line[1][0] in dic and line[1][2] in dic:
        print("huh")


def rec(result, item):
    if item == "humn":
        print(result)

    if not links[item]:
        return result
    else:
        if links[item][0] in humn_conncetion:
            val = dic[links[item][2]]
            op = links[item][1]
            if op == '-':
                return rec(result + val, links[item][0])
            elif op == "+":
                return rec(result - val, links[item][0])
            elif op == "*":
                return rec(result / val, links[item][0])
            elif op == "/":
                return rec(result * val, links[item][0])
        else:
            val = dic[links[item][0]]
            op = links[item][1]
            if op == '-':
                return rec(val - result, links[item][2])
            elif op == "+":
                return rec(result - val, links[item][2])
            elif op == "*":
                return rec(result / val, links[item][2])
            elif op == "/":
                return rec(val / result, links[item][2])


if links["root"][0] in dic:
    rec(dic[links["root"][0]], links["root"][2])
else:
    rec(dic[links["root"][2]], links["root"][0])
