print(sum(sorted([sum([int(line) for line in paragraph.split('\n')]) for paragraph in open("Day1.txt").read().split('\n\n')], reverse=True)[:3]))