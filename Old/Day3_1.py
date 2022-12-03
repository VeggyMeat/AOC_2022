import utils

file = open("Day3.txt")
text = file.read()
file.close()

dict = {}
count = 0

c = 1
for x in "abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    dict[x] = c
    c += 1

lines = text.split('\n')
for line in lines:
    backpack1 = line[:int(len(line) / 2)]
    backpack2 = line[int(len(line) / 2):]
    for item in backpack1:
        if item in backpack2:
            count += dict[item]
            break

print(count)
