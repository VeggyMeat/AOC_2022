import utils

file = open("Day4.txt")
text = file.read()
file.close()

lines = text.split('\n')

count = 0
for line in lines:
    sections = line.split(',')
    first = sections[0].split('-')
    second = sections[1].split('-')
    if list(set(range(int(first[0]), int(first[1]) + 1)).intersection(set(range(int(second[0]), int(second[1]) + 1)))):
        count += 1

print(count)
