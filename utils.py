

def paragraphs(text):
    return text.split('\n\n')


def listToInt(text):
    return [int(a) for a in text]


def lineWords(text):
    return [text.split(' ') for line in text.split('\n')]


def listUnique(l):
    for x, item1 in enumerate(l):
        for y in range(x + 1, len(l)):
            if item1 == l[y]:
                return False
    return True
