import re

day = 4
with open('in_' + str(day) + '.txt') as file:
    data = [line.strip() for line in file.readlines()]

t = 0
l = [1] * len(data)

for i, line in enumerate(data):    
    w, a = (set(re.findall('\\d+', x)) for x in line.split(': ')[1].split(' | '))
    p = len(a.intersection(w)) 

    if p >= 1:
         t += 2**(p-1)

    for idx in range(p):
        l[1+idx+i] += l[i]

print(t)
print(sum(l))
