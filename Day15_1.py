import utils

file = open("Day15.txt", 'r')
# file = open("Day15T.txt", 'r')
data = file.read()
file.close()

lines = data.split('\n')

Sensors = {}
Beacons = []
top_left = [0, 0]
bottom_right = [0, 0]

for line in lines:
    parts = line.split(': ')
    parts = [words.split(', ') for words in parts]
    sensor_cords = (int(parts[0][1][2:]), int(parts[0][2][2:]))
    beacon_cords = (int(parts[1][1][2:]), int(parts[1][2][2:]))
    if sensor_cords[0] < top_left[0]:
        top_left[0] = sensor_cords[0]
    if beacon_cords[0] < top_left[0]:
        top_left[0] = beacon_cords[0]
    if sensor_cords[1] < top_left[1]:
        top_left[1] = sensor_cords[1]
    if beacon_cords[1] < top_left[1]:
        top_left[1] = beacon_cords[1]

    if sensor_cords[0] > bottom_right[0]:
        bottom_right[0] = sensor_cords[0]
    if beacon_cords[0] > bottom_right[0]:
        bottom_right[0] = beacon_cords[0]
    if sensor_cords[1] > bottom_right[1]:
        bottom_right[1] = sensor_cords[1]
    if beacon_cords[1] > bottom_right[1]:
        bottom_right[1] = beacon_cords[1]
    dif = abs(sensor_cords[0] - beacon_cords[0]) + abs(sensor_cords[1] - beacon_cords[1])
    Sensors[sensor_cords] = dif
    Beacons.append(beacon_cords)

print(Sensors)
print(top_left, bottom_right)
y = 2000000
count = 0
for x in range(top_left[0] - 2000000, bottom_right[0] + 1 + 2000000):
    for sensor in Sensors:
        dif = abs(sensor[0] - x) + abs(sensor[1] - y)
        if dif <= Sensors[sensor]:
            count += 1
            break

print(count - 1)
