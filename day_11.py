day, test = 11, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

arr = []
for line in data:
    arr.append(line.strip())
    if line.count('#') == 0:
        arr.append('.' * len(data[0]))

c = 0
while c < len(arr[0]):
    for r in range(0, len(arr)):
        if arr[r][c] == '#':
            break
    else:
        c += 1
        for r in range(0, len(arr)):
            arr[r] = arr[r][:c] + '.' + arr[r][c:]
    c+=1

d = []
for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] == '#':
            d.append([r, c])

t = 0

while d:
    curr = d.pop()
    for e in d:
        t += abs(curr[0] - e[0]) + abs(curr[1] - e[1])

print(t)