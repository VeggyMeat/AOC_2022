import utils

file = open("Day14.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

sand_point = (500, 0)
x_offset = 350
floor = 160
grid = [['' for _ in range(350)] for y in range(161)]
grid[-1] = ['#' for _ in range(350)]

for line in lines:
    points = line.split(' -> ')
    last = (0, 0)
    for point in points:
        cart = point.split(',')
        cart = (int(cart[0]), int(cart[1]))
        if last != (0, 0):
            if cart[0] - last[0] != 0:
                for x in range(min(cart[0], last[0]), max(cart[0], last[0]) + 1):
                    grid[cart[1]][x - x_offset] = '#'
            else:
                for y in range(min(cart[1], last[1]), max(cart[1], last[1]) + 1):
                    grid[y][cart[0] - x_offset] = '#'
        last = cart


def sand_fall(cart):
    if grid[cart[1] + 1][cart[0] - x_offset] != '':
        if grid[cart[1] + 1][cart[0] - x_offset - 1] != '':
            if grid[cart[1] + 1][cart[0] - x_offset + 1] != '':
                return cart
            else:
                return sand_fall((cart[0] + 1, cart[1] + 1))
        else:
            return sand_fall((cart[0] - 1, cart[1] + 1))
    else:
        return sand_fall((cart[0], cart[1] + 1))


x = 0
while True:
    x += 1
    pos = sand_fall(sand_point)
    if pos != sand_point:
        grid[pos[1]][pos[0] - x_offset] = 'o'
    else:
        break

print(x)
