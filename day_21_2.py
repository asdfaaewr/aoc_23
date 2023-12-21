from collections import defaultdict

day, test = 21, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

data = [line.strip() for line in data]

rocks = set()

rmax = len(data)
cmax = len(data[0])

for r in range(rmax):
    for c in range(cmax):
        if data[r][c] == '#':
            rocks.add((r, c))

def get_p(r, c, n=None):
    d = defaultdict(set)
    d[0].add((r, c))

    for i in range(400):
        for r, c in d[i-1]:
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if r+dr < 0 or r+dr >= rmax or c+dc < 0 or c+dc >= cmax:
                    continue

                if (r+dr, c+dc) in rocks:
                    continue

                d[i].add((r+dr, c+dc))

            if i > 3 and len(d[i]) == len(d[i-2]) and len(d[i-1]) == len(d[i-3]):
                break

    if n is not None:
        n = d[n]

    return ([len(d[k]) for k in d]).copy(), n

r, _ = get_p(65, 65)
  
steps = 26501365 
n = (steps - rmax // 2) // rmax

u = r[::2][-1]
e = r[1::2][-1]

if steps %2 == 1:
    num_u = sum([i for i in range(2, n, 2)]) * 4 + 1
    num_e = sum([i for i in range(1, n, 2)]) * 4
else: 
    num_u = sum([i for i in range(1, n, 2)]) * 4 
    num_e = sum([i for i in range(2, n, 2)]) * 4 + 1


right_top = len(get_p(0, 130, 64)[1])
right_bot = len(get_p(130, 130, 64)[1])
left_top = len(get_p(0, 0, 64)[1])
left_bot = len(get_p(130, 0, 64)[1])

_, right_set = get_p(65, 130, 130)
_, left_set = get_p(65, 0, 130)
_, top_set = get_p(0, 65, 130)
_, bot_set = get_p(130, 65, 130)

right_or_top = len(right_set | top_set)
right_or_bot = len(right_set | bot_set)
left_or_top = len(left_set | top_set)
left_or_bot = len(left_set | bot_set)

x = len(top_set) + len(bot_set) + len(right_set) + len(left_set)
x += (n-1) * sum([right_or_top, right_or_bot, left_or_top, left_or_bot]) 

z = n * sum([right_top, right_bot, left_top, left_bot])

print(x + z + num_u * u + num_e * e)
