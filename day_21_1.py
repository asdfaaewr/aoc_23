from collections import defaultdict

day, test = 21, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

data = [line.strip() for line in data]

print(data)

d = defaultdict(set)
rocks = set()

rmax = len(data)
cmax = len(data[0])

for r in range(rmax):
    for c in range(cmax):
        if data[r][c] == '#':
            rocks.add((r, c))

d[0].add((65, 65))

for i in range(65):
    for r, c in d[i-1]:
        for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if r+dr < 0 or r+dr >= rmax or c+dc < 0 or c+dc >= cmax:
                continue

            if (r+dr, c+dc) in rocks:
                continue
            d[i].add((r+dr, c+dc))

print(len(d[64]))
        

            
