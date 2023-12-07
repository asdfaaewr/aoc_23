from collections import Counter

day = 7
with open('in_' + str(day) + '.txt') as file:
    data = file.readlines()

d = {}
for n, c in zip(range(1, 15), '123456789TJQKA'):
    d[c] = n

l = []

for line in data:
    cards, score = line.split()
    cards = [d[c] for c in cards]
    m = Counter(cards).most_common()

    t = m[0][1] + 0.5 if (m[0][1] in [2, 3] and m[1][1] == 2) else m[0][1]
    l.append([t, *cards, int(score)])

print(sum([(i+1) * e[-1] for i, e in enumerate(sorted(l))]))
