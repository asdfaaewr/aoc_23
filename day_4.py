import re
from collections import defaultdict

day = 4

with open('in_' + str(day) + '.txt') as file:
    data = [line.strip() for line in file.readlines()]

t = 0
d = defaultdict(int)


for i, line in enumerate(data):
    
    w, a = (set(re.findall('\\d+', x)) for x in line.split(': ')[1].split(' | '))

    p = len(a.intersection(w)) 
    if p >= 1:
         t += 2**(p-1)

    d[i+1] += 1
    for idx in range(p):
        d[2+idx+i] += d[i+1]

print(t)
print(sum(d.values()))
