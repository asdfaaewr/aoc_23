from collections import defaultdict, deque

day, test = 17, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

data = [line.strip() for line in data]

d = defaultdict(lambda: 1000000000)
d[(0, 0, 1, 0, 0)] = 0  #(r, c, dr, dc, steps)
d[(0, 0, 0, 1, 0)] = 0

q = deque([(0, 0, 1, 0, 0), (0, 0, 0, 1, 0)])

while q:
    r, c, dr, dc, s = q.popleft()
    if r == len(data) - 1 and c == len(data[0]) - 1 : continue

    if s < 3 and 0 <= r+dr < len(data) and 0 <= c+dc < len(data[0]):
        if d[(r+dr, c+dc, dr, dc, s+1)] > d[(r, c, dr, dc, s)] + int(data[r+dr][c+dc]):
            q.append((r+dr, c+dc, dr, dc, s+1))
            d[(r+dr, c+dc, dr, dc, s+1)] = d[(r, c, dr, dc, s)] + int(data[r+dr][c+dc])

    for x, y, in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if (x == -dr and y == dc) or (x == dr and y == -dc): continue
        if not (0 <= r+x < len(data) and 0 <= c+y < len(data[0])): continue

        if d[(r+x, c+y, x, y, 1)] > d[(r, c, dr, dc, s)] + int(data[r+x][c+y]):
            q.append((r+x, c+y, x, y, 1))
            d[(r+x, c+y, x, y, 1)] = d[(r, c, dr, dc, s)] + int(data[r+x][c+y]) 

t = 1000000000

for e in d.keys():
    if e[0] == len(data)-1 and e[1] == len(data[0])-1:
        t = min(t, d[e])
print(t)