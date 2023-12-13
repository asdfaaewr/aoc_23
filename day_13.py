day, test = 13, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read()

data = data.split('\n\n')

d = set()

def get_row(block):
    n = len(block)
    for i in range(1, n):
        l = min(i, n-i)
        if block[i-l:i][::-1] == block[i:i+l]:
            return i    
    return 0


# Part 1:
t = 0
block_nr = 0

for block in data:
    block = block.splitlines()
    block_t = [''.join([*x]) for x in zip(*block)]
    block_nr += 1

    row = get_row(block)
    d.add((block_nr, 'r', row))

    col = 0
    if row == 0:
        col = get_row(block_t)
        d.add((block_nr, 'c', col))
    
    t += 100*row + col

print(t)

# Part 2:
t = 0
block_nr = 0

for block in data:
    #print(t)
    block = block.splitlines()
    block_t = [''.join([*x]) for x in zip(*block)]
    block_nr += 1

    for r in range(len(block)):
        for c in range(len(block[0])):

            block_c = block.copy()
            block_ct = block_t.copy()

            if block_c[r][c] == '#':
                block_c[r] = block_c[r][:c] + '.' + block_c[r][c+1:]
                block_ct[c] = block_ct[c][:r] + '.' + block_ct[c][r+1:]
            else: 
                block_c[r] = block_c[r][:c] + '#' + block_c[r][c+1:]
                block_ct[c] = block_ct[c][:r] + '#' + block_ct[c][r+1:]       

            n = len(block)
            for i in range(1, n):
                l = min(i, n-i)
                if block_c[i-l:i][::-1] == block_c[i:i+l] and (block_nr, 'r', i) not in d:
                    t += i*100
                    break
       
            n = len(block_ct)
            for i in range(1, n):
                l = min(i, n-i)
                if block_ct[i-l:i][::-1] == block_ct[i:i+l] and (block_nr, 'c', i) not in d:
                    t += i
                    break


print(t//2)
