import utils

file = open("Day21.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

dic = {}

lines = [line.split(': ') for line in lines]
original = lines[:]
for line in original:
    if len(line[1].split(' ')) == 1:
        dic[line[0]] = int(line[1])
        lines.remove(line)

print(dic)

lines = [[line[0], line[1].split(' ')] for line in lines]
original = lines[:]

while "root" not in dic:
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

print(dic["root"])
