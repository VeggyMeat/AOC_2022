import utils

file = open("Day15.txt", 'r')
# file = open("Day15T.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

Sensors = {}

for line in lines:
    parts = line.split(': ')
    parts = [words.split(', ') for words in parts]
    sensor_cords = (int(parts[0][1][2:]), int(parts[0][2][2:]))
    beacon_cords = (int(parts[1][1][2:]), int(parts[1][2][2:]))
    dif = abs(sensor_cords[0] - beacon_cords[0]) + abs(sensor_cords[1] - beacon_cords[1])
    Sensors[sensor_cords] = dif

large_dif = 0
for y in range(4000001):
    x = 0
    while x < 4000001:
        a = True
        large_dif = 0
        for sensor in Sensors:
            dif = abs(sensor[0] - x) + abs(sensor[1] - y)
            if dif <= Sensors[sensor]:
                a = False
            gap = Sensors[sensor] - dif
            if gap >= large_dif:
                large_dif = gap
        if a:
            print("DAMN" + str(x * 4000000 + y))
            raise ValueError
        x += large_dif + 1
    if y % 100000 == 0:
        print(y)
