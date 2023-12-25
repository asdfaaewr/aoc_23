from sympy import solve, symbols

day, test = 24, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

l = []
for line in data:
    p, v = [list(map(int, c.strip().split(', '))) for c in line.split('@')]
    l.append((p, v))

    x0, y0, z0, vx0, vy0, vz0, n1, n2, n3, n4, n5 = symbols("x0, y0, z0, vx0, vy0, vz0, n1, n2, n3, n4, n5")

x1 = l[0][0][0]
x2 = l[1][0][0]
x3 = l[1][0][0]
x4 = l[3][0][0]                                                                                                                                 
x5 = l[4][0][0]

vx1 = l[0][1][0]
vx2 = l[1][1][0]
vx3 = l[1][1][0]
vx4 = l[3][1][0]
vx5 = l[4][1][0]

y1 = l[0][0][1]
y2 = l[1][0][1]
y3 = l[1][0][1]
y4 = l[3][0][1]
y5 = l[4][0][1]

vy1 = l[0][1][1]
vy2 = l[1][1][1]
vy3 = l[1][1][1]
vy4 = l[3][1][1]
vy5 = l[4][1][1]

z2 = l[1][0][2]
z1 = l[0][0][2]
z3 = l[1][0][2]
z4 = l[3][0][2]
z5 = l[4][0][2]

vz1 = l[0][1][2]
vz2 = l[1][1][2]
vz3 = l[1][1][2]
vz4 = l[3][1][2]
vz5 = l[4][1][2]

eqs = [
    x0 + n1*vx0 - x1 - n1*vx1,
    x0 + n2*vx0 - x2 - n2*vx2,
    x0 + n3*vx0 - x3 - n3*vx3,
    x0 + n4*vx0 - x4 - n4*vx4,
    x0 + n5*vx0 - x5 - n5*vx5,

    y0 + n1*vy0 - y1 - n1*vy1,
    y0 + n2*vy0 - y2 - n2*vy2,
    y0 + n3*vy0 - y3 - n3*vy3,
    y0 + n4*vy0 - y4 - n4*vy4,
    y0 + n5*vy0 - y5 - n5*vy5,

    z0 + n1*vz0 - z1 - n1*vz1,
    z0 + n2*vz0 - z2 - n2*vz2,
    z0 + n3*vz0 - z3 - n3*vz3,
    z0 + n4*vz0 - z4 - n4*vz4,
    z0 + n5*vz0 - z5 - n5*vz5,
]

d = solve(eqs, [x0, y0, z0, vx0, vy0, vz0, n1, n2, n3, n4, n5 ], dict=True)[0]

print(d[x0] + d[y0] + d[z0])

