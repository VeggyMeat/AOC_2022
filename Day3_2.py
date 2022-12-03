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
for x in range(0, int(len(lines) / 3)):
    backpack1 = lines[3 * x]
    backpack2 = lines[3 * x + 1]
    backpack3 = lines[3 * x + 2]
    for item in backpack1:
        print(item)
        if item in backpack2:
            if item in backpack3:
                count += dict[item]
                break
print(count)
