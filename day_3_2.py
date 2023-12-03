day = 3

with open('in_' + str(day) + '.txt') as file:
    data = [line.strip() for line in file.readlines()]

moves = ([-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1])

t = 0
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] != '*' : continue
        s = set()
        num_1, num_2 = '', ''
        for x, y in moves: 
            if num_1 == '':      
                if 0 <= r + x < len(data) and 0 <= c + y < len(data[0]):
                    if data[r+x][c+y].isdigit():
                        num_1 = data[r+x][c+y]
                        s.add((r+x, c+y))
                        if 0 <= c + y - 1< len(data[0]) and data[r+x][c+y-1].isdigit():
                            num_1 = data[r+x][c+y-1] + num_1
                            s.add((r+x, c+y-1))
                            if 0 <= c + y - 2 < len(data[0]) and data[r+x][c+y-2].isdigit():
                                num_1 = data[r+x][c+y-2] + num_1
                                s.add((r+x, c+y-2))
                        if 0 <= c + y + 1 < len(data[0]) and data[r+x][c+y+1].isdigit():
                            num_1 =  num_1 + data[r+x][c+y+1]
                            s.add((r+x, c+y+1))
                            if 0 <= c + y + 2 < len(data[0]) and data[r+x][c+y+2].isdigit():
                                num_1 = num_1 + data[r+x][c+y+2]
                                s.add((r+x, c+y+2))

            if num_1 != '':
                if 0 <= r + x < len(data) and 0 <= c + y < len(data[0]):
                    if data[r+x][c+y].isdigit() and (r+x, c+y) not in s:
                        num_2 = data[r+x][c+y]
                        s.add((r+x, c+y))
                        if 0 <= c + y - 1< len(data[0]) and data[r+x][c+y-1].isdigit():
                            num_2 = data[r+x][c+y-1] + num_2
                            s.add((r+x, c+y-1))
                            if 0 <= c + y - 2 < len(data[0]) and data[r+x][c+y-2].isdigit():
                                num_2 = data[r+x][c+y-2] + num_2
                                s.add((r+x, c+y-2))
                        if 0 <= c + y + 1 < len(data[0]) and data[r+x][c+y+1].isdigit():
                            num_2 =  num_2 + data[r+x][c+y+1]
                            s.add((r+x, c+y+1))
                            if 0 <= c + y + 2 < len(data[0]) and data[r+x][c+y+2].isdigit():
                                num_2 = num_2 + data[r+x][c+y+2]
                                s.add((r+x, c+y+2))

                if num_1 != '' and num_2 != '':
                    t += int(num_1) * int(num_2)
                    break                 

print(t)




