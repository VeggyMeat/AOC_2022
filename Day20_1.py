import utils

file = open("Day20.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')
lines = [int(x) for x in lines]
unique = set()

for n, line in enumerate(lines):
    line *= 811589153
    while True:
        if line in unique:
            if line > 0:
                line += 8115891530000
            if line < 0:
                line -= 8115891530000
        else:
            unique.add(line)
            lines[n] = line
            break

nums = lines[:]


def to_real(val):
    if val > 0:
        return val % 8115891530000
    else:
        return -(abs(val) % 8115891530000)


for _ in range(10):
    for n, line in enumerate(lines):
        value = to_real(line)
        if value != 0:
            spot = nums.index(line)
            nums.pop(spot)
            new = (spot + value) % (len(lines) - 1)
            if new == 0:
                new = len(lines) - 1
            nums.insert(new, line)

zero = nums.index(0)
print(to_real(nums[(zero + 1000) % len(nums)]), to_real(nums[(zero + 2000) % len(nums)]), to_real(nums[(zero + 3000) % len(nums)]))
print(to_real(nums[(zero + 1000) % len(nums)]) + to_real(nums[(zero + 2000) % len(nums)]) + to_real(nums[(zero + 3000) % len(nums)]))
