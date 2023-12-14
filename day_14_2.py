day, test = 14, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

data = [[*line.strip()] for line in data]
data_1 = data.copy()


def north(data):
    for c in range(len(data[0])):
        round_rock = 0
        start = 0
        for r in range(len(data)):

            if data[r][c] == 'O':
                    round_rock += 1

            if data[r][c] == '#' or r == len(data) - 1:
                for i in range(start, r + 1 * (r == len(data)-1 and data[r][c] != '#')):
                    if i < start + round_rock:
                        data[i][c] = 'O'
                    else:
                        data[i][c] = '.'
                round_rock = 0

                start = r + 1

def south(data):
    data_1 = data[::-1].copy()
    north(data_1)
    data[:] = data_1[::-1]

def west(data):
    data_1 = [[*x] for x in zip(*data.copy())]
    north(data_1)
    data[:] = [[*x] for x in zip(*data_1)]

def east(data):
    data_1 = [[*x] for x in zip(*data.copy()[::-1])]
    south(data_1)
    data[:] = [[*x] for x in zip(*data_1)][::-1]

def run_cycles(cycles, data):
    d = {}
    for cycle in range(cycles):

        s = set()
        for c in range(len(data[0])):
            for r in range(len(data)):
                if data[r][c] == 'O':
                    s.add((r, c))
            
        if s in d.values():
            for i in d.keys():
                if s == d[i]:
                    return((1000000000-i) % (cycle-i) +i )

        d[cycle] = s

        north(data)
        west(data)
        south(data)
        east(data)

cyc = run_cycles(100000000, data)
run_cycles(cyc, data_1)

t = 0
for c in range(len(data[0])):
    for r in range(len(data)):
        if data_1[r][c] == 'O':
            t += len(data_1) - r

print(t)
