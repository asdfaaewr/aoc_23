from math import lcm

day, test = 8, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read()

inst, rest = data.split('\n\n')

d = {}
for line in rest.splitlines():
    d[line[0:3]] = (line[7:10], line[12:15])

# Part 1:
curr = 'AAA'

t = 0
while True:
    curr = d[curr][0 if inst[t % len(inst)] == 'L' else 1]
    t += 1 
    if curr == 'ZZZ':
        break
print(t)


# Part 2:
curr_list = [x for x in d.keys() if x[2]=='A']

q = {}
for curr in curr_list:
    t = 0
    start = curr
    while True:
        if curr in q:
            q[start] = t + q[curr]
            break

        curr = d[curr][0 if inst[t % len(inst)] == 'L' else 1]        
        t += 1 
        
        if curr[2] == 'Z':
            q[start] = t
            break

print(lcm(*q.values()))