import utils

file = open("Day2.txt")
text = file.read()
file.close()

lines = text.split('\n')
#lines = ["A Y", "B X", "C Z"]
dict1= {"A": 1, "B": 2, "C": 3}
dict2= {"X":1, "Y":2, "Z":3}
points = 0
for line in lines:
    terms = line.split(' ')
    if dict1[terms[0]] % 3 == (dict2[terms[1]] - 1) % 3:
        points += 6 + dict2[terms[1]]
    elif dict1[terms[0]] == dict2[terms[1]]:
        points += 3 + dict2[terms[1]]
    else:
        points += dict2[terms[1]]

print(points)