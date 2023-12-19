import re
from math import prod

day, test = 19, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    instructions, points = file.read().split('\n\n')

d = {}
for line in instructions.splitlines():
    name, conditions = line[:-1].split('{')
    d[name] = conditions.split(',')

stack = [('in', (1, 4000), (1, 4000), (1, 4000), (1, 4000))]
t = 0

while stack:
    name, x, m, a, s = stack.pop()
    v = [x, m, a, s]

    if name == 'R':
        continue
    if name == 'A':
        t += prod([e[1]-e[0]+1 for e in v])
        continue

    for inst in d[name]:
        condition, *target = inst.split(':')
        v_new = v.copy()

        if target == []:
            stack.append((condition, *v))
        else:
            for i in range(4):
                if condition[0] == 'xmas'[i]:
                    if condition[1] == '<':
                        v_new[i] = (v[i][0], min(v[i][1], int(condition[2:])-1))
                        v[i] = (max(v[i][0], int(condition[2:])), v[i][1])
                    else:
                        v_new[i] = (max(v[i][0], int(condition[2:])+1), v[i][1])
                        v[i] = (v[i][0], min(v[i][1], int(condition[2:])))

                    stack.append((target[0], *v_new))
print(t)