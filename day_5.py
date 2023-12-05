import re
import heapq

day = 5
with open('in_' + str(day) + '.txt') as file:
    data =  file.read().split('\n\n')

seeds = re.findall('\\d+', data[0])

ds = []
for i, block in enumerate(data[1:]):
    d = {}
    for line in block.splitlines()[1:]:
        dest, source, length = list(map(int, line.split()))
        d[range(source, source+length)] = dest-source

    ds.append(d)    

# Part 1: 

def f(k, d):
    for key in d.keys():
        if k in key:
            return k + d[key]
    return k

def comb_funs(k, ds):
    for i in range(len(ds)):
        k = f(k, ds[i])    
    return k

print(min([comb_funs(int(seed), ds) for seed in seeds]))

# Part 2:

seeds = [(int(a), int(a)+int(b)-1) for a,b in zip(seeds[::2], seeds[1::2])]
   
for i in range(len(ds)):
    new_seeds = []

    for r in seeds:
        h = list(ds[i].keys())
        heapq.heapify(h)
        while r[1] >= r[0]:
            if len(h) == 0:
                new_seeds.append(r)
                break
            a = heapq.heappop(h)
            if r[0] > a[1]:
                continue
            if r[0] < a[0]:
                new_seeds.append((r[0], min(r[1], a[0])))
                heapq.heappush(h, a)
                r = min(r[1], a[0]) + 1, r[1] 
            else:
                new_seeds.append((r[0] + ds[i][a], min(r[1], a[1]) + ds[i][a]))
                r = min(r[1], a[1]) + 1, r[1] 

    seeds = new_seeds

print(min([x[0] for x in seeds])) 