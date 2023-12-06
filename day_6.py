day = 6
with open('in_' + str(day) + '.txt') as file:
    times, dists =  file.readlines()
    times = list(map(int, times.split(':')[1].split()))
    dists = list(map(int, dists.split(':')[1].split()))

# Part 1:
p = 1
for time, dist in zip(times, dists):
    t = 0
    for i in range(1, time):
        if i * (time-i) > dist:
            t += 1 
    p *= t
print(p)

# Part 2:
time = int(''.join([str(t) for t in times]))
dist = int(''.join([str(d) for d in dists]))

t = 0
for i in range(1, time):
    if i * (time-i) > dist:
        t += 1 
print(t)

# More general:
print(2 * int((time**2/4 - dist)**0.5) + 1)