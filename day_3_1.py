day = 3

with open('in_' + str(day) + '.txt') as file:
    data = [line.strip() for line in file.readlines()]

moves = ([-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1])

t = 0
for r in range(len(data)):
    c = 0
    while c < len(data[0]):
        num, flag = '', False
        while c < len(data[0]) and data[r][c].isdigit():
            num += data[r][c]
            for x, y in moves:
                if 0 <= r + x < len(data) and 0 <= c + y < len(data[0]):
                    if not (data[r+x][c+y].isdigit() or data[r+x][c+y] == '.'):
                        flag = True
            c += 1
        if flag : t += int(num)
        c += 1

print(t)




