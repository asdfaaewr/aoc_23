day, test = 16, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

data = [line.strip() for line in data]

beams = set([(0, -1, 0, 1)])
seen = beams.copy()
new_beams = set()
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

    beams = new_beams.copy() 
    
print(len(energized))           