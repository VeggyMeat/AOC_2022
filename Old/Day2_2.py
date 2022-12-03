import utils

file = open("Day2.txt")
text = file.read()
file.close()

lines = text.split('\n')
#lines = ["A X", "B X", "C Z"]
dict1= {"A": 1, "B": 2, "C": 3}
dict2= {"X":1, "Y":2, "Z":3}
points = 0
for line in lines:
    terms = line.split(' ')
    if dict2[terms[1]] == 1:
        points += 0 + (dict1[terms[0]] - 2) % 3 + 1
    elif dict2[terms[1]] == 2:
        points += 3 + dict1[terms[0]]
    else:
        points += 6 + dict1[terms[0]] % 3 + 1
    print(points)

print(points)