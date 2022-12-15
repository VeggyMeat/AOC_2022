import utils

file = open("Day15.txt", 'r')
# file = open("Day15T.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

Sensors = {}
Beacons = []

for line in lines:
    parts = line.split(': ')
    parts = [words.split(', ') for words in parts]
    sensor_cords = (int(parts[0][1][2:]), int(parts[0][2][2:]))
    beacon_cords = (int(parts[1][1][2:]), int(parts[1][2][2:]))
    dif = abs(sensor_cords[0] - beacon_cords[0]) + abs(sensor_cords[1] - beacon_cords[1])
    Sensors[sensor_cords] = dif
    Beacons.append(beacon_cords)

print(Sensors)
y = 2000000
count = 0
for x in range(-2000000, 6000000):
    for sensor in Sensors:
        dif = abs(sensor[0] - x) + abs(sensor[1] - y)
        if dif <= Sensors[sensor]:
            count += 1
            break

print(count - 1)
