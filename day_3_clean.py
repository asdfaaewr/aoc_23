from collections import defaultdict
day = 3

with open('in_' + str(day) + '.txt') as file:
    data = [line.strip() for line in file.readlines()]

moves = ([-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1])

t = 0
d = defaultdict	(list)

for r in range(len(data)):
    c = 0
    while c < len(data[0]):
        num, flag, flag_star = '', False, False
        while c < len(data[0]) and data[r][c].isdigit():
            num += data[r][c]
            for x, y in moves:
                if 0 <= r + x < len(data) and 0 <= c + y < len(data[0]):
                    if not (data[r+x][c+y].isdigit() or data[r+x][c+y] == '.'):
                        flag = True
                    if data[r+x][c+y] == '*':
                        star_at = (r+x, c+y)
                        flag_star = True
            c += 1
        if flag: t += int(num)
        if flag_star: d[star_at].append(int(num)) 
        c += 1

print(t)
print(sum(v[0] * v[1] for v in d.values() if len(v)==2))





