from collections import deque
import math

day, test = 20, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

d = {}
for line in data:
    module, target = line.split(' -> ')
    if module == 'broadcaster':
        beams = [(b.strip(), 0) for b in target.split(', ')]
    else:
        d[module[1:]] = [module[0], [b.strip() for b in target.split(', ')], 0 if module[0] == '%' else {}]

for m1 in d:
    if d[m1][0] == '&':
        for m2 in d:
            if m1 in d[m2][1]:
                d[m1][2][m2] = 0
                

periods = [0] * len(*[d[e][2] for e in d if 'rx' in d[e][1]])

for k in range(1, 10_000):
    q = deque(beams)

    while q:
        target, intensity = q.popleft()

        if d[target][0] == '%':
            if intensity == 1:
                continue

            if d[target][2] == 0:
                intensity = 1

            d[target][2] ^= 1

        
        if d[target][0] == '&':
            if all(d[target][2].values()) == 1:
                intensity = 0
            else:
                intensity = 1

        for t in d[target][1]:
            if t not in d: 
                if t == 'rx':
                    for i, m in enumerate(d[target][2].values()):
                        if m == 1 and periods[i] == 0:
                            periods[i] = k

                            if min(periods) > 0:
                                print(math.lcm(*periods))
                                exit(0)

                continue

            q.append((t, intensity))
            if d[t][0] == '&':
                d[t][2][target] = intensity
