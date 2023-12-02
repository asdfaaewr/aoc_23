from collections import defaultdict
import math 

day = 2

with open('in_' + str(day) + '.txt') as file:
    data = file.readlines()

t = 0
p = 0

for i, line in enumerate(data):
    _, games = line.split(':')
    games = games.split(';')
    d = defaultdict(int)
    for game in games:
        for cube in [x.strip() for x in game.split(',')]:
            num, color = cube.split()
            d[color] = max(d[color], int(num))

    if d['red'] <= 12 and d['green'] <= 13 and d['blue'] <= 14:
        t += i+1
    p += math.prod(d.values())

print(t)
print(p) 