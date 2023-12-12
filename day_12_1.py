day, test = 12, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

def get_sum(rec, dam, block_started=0, block_ended=0):

    if dam == []:
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
            g = get_sum(rec[1:], [dam[0]-1, *dam[1:]], 1, 0)
        else:
            g = get_sum(rec[1:], dam[1:], 0, 1)

    return f + g

t = 0
for line in data:
    rec, dam = line.split(' ')
    dam = list(map(int, dam.split(',')))
    t += get_sum(rec, dam)

print(t)
