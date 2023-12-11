day, test = 11, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

arr = []
r_idx =[]
c_idx = []

for r, line in enumerate(data):
    arr.append(line.strip())
    if line.count('#') == 0:
        r_idx.append(r)

for c in range(0, len(arr[0])):
    for r in range(0, len(arr)):
        if arr[r][c] == '#':
            break
    else:
        c_idx.append(c)

d = []
for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] == '#':
            d.append([r, c])

t = 0
scale = 1_000_000

while d:
    curr = d.pop()
    for e in d:
        start = min(curr[1], e[1])
        off_1 = sum([1 for i in range(min(curr[0], e[0]), max(curr[0], e[0])) if i in r_idx])
        off_2 = sum([1 for i in range(min(curr[1], e[1]), max(curr[1], e[1])) if i in c_idx])
        t += abs(curr[0] - e[0]) + abs(curr[1] - e[1]) + off_1 * (scale-1) + off_2 * (scale-1)

print(t)