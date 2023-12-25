from collections import deque

day, test = 23, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

data = [line.strip() for line in data]

stack = deque([((0, 1), set())])

rmax = len(data)
cmax = len(data[0])

t = 0
i = 0

while stack:
    curr, path = stack.pop()
    r, c = curr
    path.add((r, c))

    for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:

        if r + dr < 0: continue

        if (r+dr, c+dc) in path: continue

        if data[r+dr][c+dc] == '#':
            continue
        path_c = path.copy()
        if (r+dr, c+dc) in path: continue

        if data[r+dr][c+dc] in '<>^v':
            if dr == 1 and data[r+dr][c+dc] == 'v' or \
            dr == -1 and data[r+dr][c+dc] == '^' or \
            dc == 1 and data[r+dr][c+dc] == '>'  or \
            dc == -1 and data[r+dr][c+dc] == '<':
                path_c.add((r+dr, c+dc))
                dr *= 2
                dc *= 2
            else:
                continue
            
        if (r+dr, c+dc) in path_c: continue


        if r + dr == rmax - 1:        
            t = max(t, len(path_c))
            continue

        stack.append(((r+dr, c+dc), path_c.copy()))




print(t)

# for r in range(rmax):
#     print(''.join([data[r][c] if (r, c) not in out else 'O' for c in range(cmax)]))
#     #
#     # print(''.join([data[r][c] for c in range(cmax)]))



