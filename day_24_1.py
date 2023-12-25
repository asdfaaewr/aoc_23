day, test = 24, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

l = []
for line in data:
    p, v = [list(map(int, c.strip().split(', '))) for c in line.split('@')]
    l.append((p, v))

lo = 200000000000000
hi = 400000000000000

t = 0

for i, c1 in enumerate(l):
    x1, y1, z1 = c1[0]
    vx1, vy1, vz1 = c1[1]
    for c2 in l[i+1:]:
        x2, y2, z2 = c2[0]
        vx2, vy2, vz2 = c2[1]

        if vy2*vx1 - vx2*vy1 == 0:
            continue

        a = (vx2 * (y1-y2) - vy2 * (x1-x2)) / (vy2*vx1 - vx2*vy1)
        b = ((x1-x2) + vx1*a) / vx2 
        x = (x1 + vx1*a)
        y = (y1 + vy1*a)

        if lo <= x <= hi and lo <= y <= hi and a > 0 and b > 0:
            t += 1
print(t)
