day, test = 22, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

bricks = []
for line in data:
    p1, p2 = [tuple(map(int, c.split(','))) for c in line.strip().split('~')]
    ranges = [*zip(p1, p2)]
    brick = set()
    for x in range(ranges[0][0], ranges[0][1]+1):
        for y in range(ranges[1][0], ranges[1][1]+1):
            for z in range(ranges[2][0], ranges[2][1]+1):
                brick.add((x, y, z))
    bricks.append(brick)

def fall():
    cont = True
    fall_set = set()
    while cont:
        cont = False
        for i, b in enumerate(bricks):
            falls = True
            for x, y, z in b:    
                for j, other_b in enumerate(bricks):
                    if i == j: continue

                    if (x, y, z-1) in other_b or z <= 1:
                        falls = False
                        break

                if falls == False:
                    break

            if falls: 
                bricks[i] = [(x, y, z-1) for x, y, z in b]
                fall_set.add(i)
                #print(i)
                cont = True
    return len(fall_set)
        
fall()                
bricks_o = bricks.copy()

k = 0
t = 0
for i, b in enumerate(bricks):
    bricks[i] = {(0, 0, -1)} 
    t += fall()
    bricks = bricks_o.copy()
    k += 1
    print(k)
print(t)




            
