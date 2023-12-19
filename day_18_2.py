day, test = 18, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

s = set()
start = (0, 0)
for line in data:
    *_, st = line.split()
    n = int(st[2:7], 16)
    d = st[7]

    if d == '0':        
        s.add((start, (start[0], start[1] + int(n))))
        start = (start[0], start[1] + int(n))
    if d == '2':
        s.add((start, (start[0], start[1] - int(n))))
        start = (start[0], start[1] - int(n))
    if d == '3':
        s.add(((start[0] + int(n), start[1]), start))
        start = (start[0] + int(n), start[1])
    if d == '1':
        s.add(((start[0] - int(n), start[1]), start))
        start = (start[0] - int(n), start[1])

points = set([e1  for e1, e2 in s] + [e2  for e1, e2 in s])
points = sorted(points)[::-1]

rows_t = sorted(list(set([p[0] for p in points])))[::-1]
rows = sorted(list(set(rows_t + [r-1 for r in rows_t[:-1]])))[::-1]
rows = sorted(list(set(rows + [r+1 for r in rows_t[1:]])))[::-1]

cols = sorted(list(set([p[1] for p in points])))[::-1]

new_points = set()
for e in s:
    for row in rows:
        if min(e[0][0], e[1][0]) < row < max(e[0][0], e[1][0]):
            new_points.add((row, e[0][1]))

points = sorted(list(set(points) | new_points))[::-1]

t = 0

for r1, r2 in zip(rows[:-1], rows[1:]):
    p_in_row = sorted([p[1] for p in points if p[0] == r2])
    inside = True
    for p1, p2 in zip(p_in_row[:-1], p_in_row[1:]):
        if ((r2, p1), (r2, p2)) not in s and ((r2, p2), (r2, p1)) not in s:
            if inside:
                t += abs(r1-r2) * (p2-p1-1)
            inside = not inside

        if ((r2, p1), (r2, p2)) in s or ((r2, p2), (r2, p1)) in s:
            max_r = max([max([a[0] for a in e]) for e in s if (r2, p1) in e])
            max_r = max(max_r, max([max([a[0] for a in e]) for e in s if (r2, p2) in e]))
            min_r = min([min([a[0] for a in e]) for e in s if (r2, p1) in e])
            min_r = min(min_r, min([min([a[0] for a in e]) for e in s if (r2, p2) in e]))

            if r2 == max_r or r2 == min_r:
                inside = not inside 

print(t+sum([abs(p1[0]-p2[0]) + abs(p1[1] - p2[1]) for p1, p2 in s]))
