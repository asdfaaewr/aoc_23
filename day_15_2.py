from collections import defaultdict

day, test = 15, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().split(',')

def hash(string):
    q = 0
    for ch in string:
        q = ((q + ord(ch))*17) % 256
    return q    

d = defaultdict(list)

for s in data:

    if s[-1] == '-':
        op, lens = '-', s[:-1]
    else:
        op, lens, fl = '=', s[:-2], s[-1]

    for i, v in enumerate(d[hash(lens)]):
        if v[0] == lens:
            if op == '=':
                d[hash(lens)][i] = (lens, fl)
            else: 
                d[hash(lens)] = d[hash(lens)][:i] + d[hash(lens)][i+1:]
            break
    else:
        if op == '=':
            d[hash(lens)].append((lens, fl))
    

t = 0    
for k in d.keys():
    for i, e in enumerate(d[k]):
        t += (i+1) * (k+1) * int(e[1])
print(t)