day, test = 10, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

data = [line.strip() for line in data]

for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == "S":
            r_s, c_s = r, c
            break

stack = []
seen = set()
seen.add((r_s, c_s))
s_in = set(['J', '7', '-', '|', 'F', 'L'])

for x, y, in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
    if r_s + x < 0 or r_s + x >= len(data) or c_s + y < 0 or c_s + y >= len(data[0]):
        continue

    if x == -1 and data[r_s+x][c_s] in ["F", "|", "7"]:
        stack.append((r_s+x, c_s))
        seen.add((r_s+x, c_s))
        s_in &= set(['|', 'L', 'J'])
        

    if x == 1 and data[r_s+x][c_s] in ["L", "|", "J"]:
        stack.append((r_s+x, c_s))
        seen.add((r_s+x, c_s))
        s_in &= set(["F", "|", "7"])
        

    if y == -1 and data[r_s][c_s+y] in ["F", "-", "L"]:
        stack.append((r_s, c_s+y))
        seen.add((r_s, c_s+y))
        s_in &= set(["7", "-", "J"])
        

    if y == 1 and data[r_s][c_s+y] in ["7", "-", "J"]:
        stack.append((r_s, c_s+y))
        seen.add((r_s, c_s+y))
        s_in &= set(["F", "-", "L"])

while stack:

    r, c = stack.pop()
    seen.add((r, c))

    for x, y, in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if r + x < 0 or r + x >= len(data) or c + y < 0 or c + y >= len(data[0]):
            continue

        if x == -1 and data[r][c] in ["L", "|", "J"] and data[r+x][c] in ["F", "|", "7"] and (r+x, c) not in seen:
            stack.append((r+x, c))      

        if x == 1 and data[r][c] in ["F", "|", "7"] and data[r+x][c] in ["L", "|", "J"] and (r+x, c) not in seen:
            stack.append((r+x, c))

        if y == -1 and data[r][c] in ["7", "-", "J"] and data[r][c+y] in ["F", "-", "L"] and (r, c+y) not in seen:
            stack.append((r, c+y))

        if y == 1 and data[r][c] in ["F", "-", "L"] and data[r][c+y] in ["7", "-", "J"] and (r, c+y) not in seen:
            stack.append((r, c+y))



print(len(seen)//2)

# Part 2 (There are much simpler solutions - don't bother reading...)
    
data[r_s] = data[r_s][:c_s] + list(s_in)[0] + data[r_s][c_s+1:]

data_new = [''.join([data[r//2][c] + '§' for c in range(len(data[0]))]) if r%2 == 0 else '§'*(len(data[0])*2) for r in range(2*len(data)-1)]

loop = set()
for s in seen:
    x, y = s
    loop.add((2*x, 2*y ))
    

for r in range(0, len(data_new)):
    for c in range(0, len(data_new[0])-1):
        if data_new[r][c] != "§": continue

        if r > 0 and (r-1, c) in loop and (r+1, c) in loop:
            if data_new[r-1][c] in ["F", "|", "7"] and data_new[r+1][c] in ["|", "L", "J"]:
                data_new[r] = data_new[r][:c] + '|' + data_new[r][c+1:]
                loop.add((r, c))

        if c > 0 and (r, c-1) in loop and (r, c+1) in loop:
            if data_new[r][c-1] in ["F", "-", "L"] and data_new[r][c+1] in ["-", "7", "J"]:
                data_new[r] = data_new[r][:c] + '-' + data_new[r][c+1:]
                loop.add((r, c))


for r in range(0, len(data_new)):
    for c in [0, len(data_new[0])-1]:

        if (r, c) in loop: continue

        stack = [(r, c)]

        while stack:
            row, col = stack.pop()
            loop.add((row, col))

            for x, y, in [[-1, 0], [1, 0], [0, -1], [0, 1]]:

                if row + x < 0 or row + x >= len(data_new) or col + y < 0 or col + y >= len(data_new[0]):
                    continue
                
                if (row + x, col + y) not in loop:                 
                    stack.append((row + x, col + y))

for r in [0, len(data_new)-1]:
    for c in range(0, len(data_new[0])):

        if (r, c) in loop: continue
        loop.add((r, c))

        stack = [(r, c)]

        while stack:
            row, col = stack.pop()
            loop.add((row, col))

            for x, y, in [[-1, 0], [1, 0], [0, -1], [0, 1]]:

                if row + x < 0 or row + x >= len(data_new) or col + y < 0 or col + y >= len(data_new[0]):
                    continue
                
                if (row + x, col + y) not in loop:                 
                    stack.append((row + x, col + y))

t = 0
for r in range(0, len(data_new)-1):
    for c in range(0, len(data_new[0])-1):
        if (r,c) in loop: continue
        if data_new[r][c] == "§": continue
        t+=1

print(t)