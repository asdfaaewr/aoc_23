day, test = 15, 1
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().split(',')

t = 0
for s in data:
    q = 0
    for ch in s:
        q = ((q + ord(ch))*17) % 256
    
    t += q

print(t)