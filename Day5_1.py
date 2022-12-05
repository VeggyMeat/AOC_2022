import utils

file = open("Day5.txt")
text = file.read()
file.close()

lines = text.split('\n')
stacks = [["F", "C", "P", "G", "Q", "R"],
          ["W", "T", "C", "P"],
          ["B", "H", "P", "M", "C"],
          ["L", "T", "Q", "S", "M", "P", "R"],
          ["P", "H", "J", "Z", "V", "G", "N"],
          ["D", "P", "J"],
          ["L", "G", "P", "Z", "F", "J", "T", "R"],
          ["N", "L", "H", "C", "F", "P", "T", "J"],
          ["G", "V", "Z", "Q", "H", "T", "C", "W"]]

for line in lines:
    sections = line.split(' ')
    number = int(sections[1])
    from_stack = int(sections[3]) - 1
    to_stack = int(sections[5]) - 1
    for x in range(number):
        stacks[to_stack].append(stacks[from_stack].pop(-1))

for stack in stacks:
    print(stack[-1], end='')