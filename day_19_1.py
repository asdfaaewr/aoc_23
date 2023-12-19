import re

day, test = 19, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    instructions, points = file.read().split('\n\n')

d = {}
for line in instructions.splitlines():
    name, conditions = line[:-1].split('{')
    d[name] = conditions.split(',')

t = 0
for point in points.splitlines():
    x, m, a, s = map(int, re.findall('\\d+', point))

    name = 'in'
    sub = -1
    while sub < 0:
        for inst in d[name]:
            condition, *target = inst.split(':')

            if target == [] or eval(condition):
                if target == []:
                    target = [condition]

                if target[0] == 'A':
                    sub = x + m + a + s
                if target[0] == 'R':
                    sub = 0
                
                name = target[0]
                break
    t += sub

print(t)
                