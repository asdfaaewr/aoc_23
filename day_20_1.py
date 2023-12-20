from collections import deque

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


low_pulses, high_pulses = 0, 0

for _ in range(1000):
    q = deque(beams)
    low_pulses += len(beams) + 1

    while q:
        target, intensity = q.pop()
        
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
            high_pulses += intensity
            low_pulses += (1-intensity)

            if t not in d: continue

            q.append((t, intensity))
            if d[t][0] == '&':
                d[t][2][target] = intensity

print(low_pulses * high_pulses)