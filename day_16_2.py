day, test = 16, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

data = [line.strip() for line in data]

t = 0

for start_row in range(len(data)): 
    for start_col in range(len(data[0])): 

        if 0 < start_row < len(data)-1 and 0 < start_col < len(data[0])-1:
            continue

        if start_col == 0:
            beams = set([(start_row, start_col -1 , 0, 1)])
        if start_col == len(data[0])-1: 
            beams = set([(start_row, start_col + 1, 0, -1)])
        if start_row == 0:
            beams = set([(start_row - 1, start_col, 1, 0)])
        if start_row == len(data)-1:
            beams = set([(start_row + 1, start_col, -1, 0)])

        seen = beams.copy()
        energized = set()

        while True:
            x = len(seen)
            new_beams = set()

            for beam in beams:
                r, c, dr, dc = beam
                r += dr
                c += dc

                if r >= len(data) or c >= len(data[0]) or r < 0 or c < 0:
                    continue

                energized.add((r, c))

                if data[r][c] == '.':
                    new_beams.add((r, c, dr, dc))
                
                if data[r][c] == '/':
                    new_beams.add((r, c, -dc, -dr))

                if data[r][c] == '\\':
                    new_beams.add((r, c, dc, dr))

                if data[r][c] == '-':
                    if dr == 0:
                        new_beams.add((r, c, 0, dc))

                    if dc == 0:
                        new_beams.add((r, c, 0, -1))
                        new_beams.add((r, c, 0, 1))

                if data[r][c] == '|':
                    if dr == 0:
                        new_beams.add((r, c, 1, 0))
                        new_beams.add((r, c, -1, 0))

                    if dc == 0:
                        new_beams.add((r, c, dr, 0))


            beams = new_beams - seen 
            seen |= new_beams

            if x == len(seen):
                break

        t = max(t, len(energized))

print(t)