import utils

file = open("Day6.txt", "r")
data = file.read()
file.close()

for x in range(4, len(data)):
    chars = data[x-4:x]
    print(chars)
    go = True
    for a in range(len(chars)):
        for b in range(a + 1, len(chars)):
            if chars[a] == chars[b]:
                go = False
                break
    if go:
        print(x)
        break

