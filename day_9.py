day, test = 9, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

t1, t2 = 0, 0

for line in data:
    line = list(map(int, line.split()))
    boarder = [] 
    boarder_left = []
    while max(line) != 0 or min(line) != 0:
        boarder.append(line[-1])
        boarder_left.append(line[0])
        line = [line[i] - line[i-1] for i in range(1, len(line))]

    s = 0
    for e in boarder_left[::-1]:
        s = e-s

    t1 += sum(boarder) 
    t2 += s 

print(t1)
print(t2)


