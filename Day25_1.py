import utils

file = open("Day25.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

total = 0
for line in lines:
    multp = 1
    for char in line[::-1]:
        if char == '=':
            total -= 2 * multp
        elif char == '-':
            total -= multp
        else:
            total += int(char) * multp
        multp *= 5

out = []
stop = False
while total != 0:
    mod = total % 5
    if mod == 0:
        out.insert(0, "0")
    if mod == 1:
        out.insert(0, "1")
    if mod == 2:
        out.insert(0, "2")
    if mod == 3:
        out.insert(0, "=")
        total += 2
    if mod == 4:
        out.insert(0, "-")
        total += 1
    total //= 5

print(''.join(out))
