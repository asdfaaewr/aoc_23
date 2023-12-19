day, test = 18, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

pos = (0, 0)
s = {(0, 0)}
for line in data:
    d, n, *_ = line.split()
    for i in range(1, int(n)+1):
        if d == 'R':
            dr, dc = 0, 1
        if d == 'L':
            dr, dc = 0, -1
        if d == 'U':
            dr, dc = -1, 0
        if d == 'D':
            dr, dc = 1, 0

        pos = (pos[0] + dr, pos[1] + dc)
        s.add(pos)

min_r = min([a[0] for a in s])
max_r = max([a[0] for a in s])
min_c = min([a[1] for a in s])
max_c = max([a[1] for a in s])

s_old = s.copy()

for r in range(min_r, max_r+1):

    c = min_c
    inside = False

    r_curr_max = max([a[1] for a in s_old if a[0] == r])
    while c < r_curr_max:
        flip = False
        if (r, c) in s_old and (r, c-1) not in s_old:
            flip = True
        
        over, under = False, False
        while (r, c) in s_old and c < r_curr_max:
            if (r-1, c) in s_old:
                over = True
            if (r+1, c) in s_old:
                under = True
            c += 1

        if flip and over and under:
            inside = not inside 
                           
        if inside:
            s.add((r, c))
        
        c += 1

print(len(s))
