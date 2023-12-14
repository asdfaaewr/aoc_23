day, test = 14, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

data = [[*line.strip()] for line in data]

for c in range(len(data[0])):
    round_rock = 0
    start = 0
    for r in range(len(data)):

        if data[r][c] == 'O':
                round_rock += 1

        if data[r][c] == '#' or r == len(data) - 1:
            for i in range(start, r + 1 * (r == len(data)-1)):
                if i < start + round_rock:
                    data[i][c] = 'O'
                else:
                    data[i][c] = '.'
            round_rock = 0
            start = r + 1

t = 0
for c in range(len(data[0])):
    for r in range(len(data)):
        if data[r][c] == 'O':
            t += len(data) - r

print(t)
