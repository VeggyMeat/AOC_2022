file = open("Day1.txt")
text = file.read()
file.close()
lines = text.split('\n')
a = []
b = 0
for line in lines:
    if line == "":
        a.append(int(b))
        b = 0
    else:
        b += int(line)
a.append(b)
print(max(a))
