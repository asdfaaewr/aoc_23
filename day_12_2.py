day, test = 12, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

d = {}

def get_sum(rec, dam, block_started=0, block_ended=0):

    if (rec, dam, block_started, block_ended) in d.keys():
        return d[(rec, dam, block_started, block_ended)]

    if dam == ():
        if rec.count('#') > 0:
            return 0
        else:
            return 1

    if sum(dam) > rec.count('#') + rec.count('?') or len(rec) == 0:
        return 0

    f, g = 0, 0

    if rec[0] in ['.', '?'] and block_started == 0:
        f = get_sum(rec[1:], dam)

    if rec[0] in ['?', '#'] and block_ended == 0:
        if dam[0] > 1:
            g = get_sum(rec[1:], tuple([dam[0]-1, *dam[1:]]), 1, 0)
        else:
            g = get_sum(rec[1:], tuple(dam[1:]), 0, 1)

    d[(rec, dam, block_started, block_ended)] = f + g
    return f + g

t = 0
for line in data:
    rec, dam = line.split(' ')
    rec = ''.join([rec + '?' for _ in range(5)])[:-1]
    dam = tuple(map(int, dam.split(','))) * 5
    t += get_sum(rec, dam)

print(t)