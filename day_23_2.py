from collections import deque

day, test = 23, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

data = [line.strip() for line in data]

stack = deque([((0, 1), (0, 0), [], 0, (0, 0))])

rmax = len(data)
cmax = len(data[0])

d = {}
dead_end = set()

while stack:
    curr, last, directions, steps, start  = stack.pop()
    r, c = curr

    eligible = []
    for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:

        if r + dr < 0: continue
        if data[r+dr][c+dc] == '#' or (r+dr, c+dc) == last: continue

        eligible.append((r+dr, c+dc))

    if len(eligible) == 0:
        dead_end.add(start)

    if len(eligible) == 1:

        if eligible[0][0] == rmax - 1:
            d[start] = (eligible, steps)
            continue

        stack.append((eligible[0], (r, c), directions, steps+1, start))
        
    if len(eligible) >= 2:
        if start in d and d[start] == (eligible, steps, (r, c)): 
            continue
        d[start] = (eligible, steps, (r, c))
        for eli in eligible:
            stack.append((eli, (r, c), directions, 1, eli))

print('phase 2')

stack =[((0,0), 1, set())]
t = 0
while stack:
    start, steps, seen = stack.pop()
    
    if start not in d:
        continue
    
    if len(d[start]) == 2:
        #print(t)
        t = max(t, steps + d[start][1])
        continue

    steps += d[start][-2]

    for des in d[start][0]:
        if des not in seen and des not in dead_end and d[start][-1] not in seen:
            seen_c = seen.copy()
            seen_c.add(d[start][-1])
            seen_c.add(des)
            stack.append((des, steps, seen_c.copy()))
        
print(t)
