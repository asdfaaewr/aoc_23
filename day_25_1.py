from collections import defaultdict
import networkx as nx

day, test = 25, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

data = [line.strip() for line in data]

d = defaultdict(list)
all_nodes = set()

for line in data:
    a, b = line.split(': ')
    for e in b.split(): 
        d[a].append(e)
        d[e].append(a)
        all_nodes.add(a)
        all_nodes.add(e)

def remove(d, y, x):
    d1 = d.copy()
    d1[x] = [e for e in d1[x] if e != y]
    d1[y] = [e for e in d1[y] if e != x]       

    return d1

def count_nodes(d, node):
    seen = set()
    stack = [node]

    while stack:
        node = stack.pop()
        seen.add(node)

        for des in d[node]:
            if des not in seen:
                stack.append(des)

    return (len(seen))

g = nx.Graph()
for line in data:
    a, b = line.split(': ')
    g.add_node(a) 
    for e in b.split():
        g.add_node(e)
        g.add_edge(a, e)

to_remove = list(nx.minimum_edge_cut(g))

d1 = remove(d, *to_remove[0])
d2 = remove(d1, *to_remove[1])
d3 = remove(d2, *to_remove[2])

x = count_nodes(d3, 'btk')
print(x*(len(all_nodes)-x))