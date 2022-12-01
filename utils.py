

def paragraphs(text):
    return text.split('\n\n')


def listToInt(text):
    return [int(a) for a in text]


def lineWords(text):
    return [text.split(' ') for line in text.split('\n')]
