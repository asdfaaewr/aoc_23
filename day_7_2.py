from collections import Counter

day = 7
with open('in_' + str(day) + '.txt') as file:
    data = file.readlines()

d = {}
for n, c in zip(range(0, 14), 'J123456789TQKA'):
    d[c] = n

l = []

for line in data:
    cards, score = line.split()
    cards = [d[c] for c in cards]

    counter = Counter(cards)
    js = counter[0]
    counter[0] = 0
    m = counter.most_common()

    t = m[0][1] + js + 0.5 if (m[0][1] + js in [2, 3] and m[1][1] == 2) else m[0][1] + js
    l.append([t, *cards, int(score)])

print(sum([(i+1) * e[-1] for i, e in enumerate(sorted(l))]))
