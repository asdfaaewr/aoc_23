import re

day = 1

with open('in_' + str(day) + '.txt') as file:
    data = file.readlines()

# Part 1
t=0
for line in data:
    t += int(re.findall('\d', line)[0] + re.findall('\d', line)[-1])

print(t)

# Part 2
d = {'one' : '1', 'two' : '2', 'three' : '3', 'four': '4', 'five' : '5',
     'six' : '6', 'seven' : '7' , 'eight' : '8', 'nine' : '9'}

p = re.compile('(?=(\d|' + '|'.join(d.keys()) + '))')

t = 0
for line in data:
    s = [n if n.isnumeric() else d[n] for n in re.findall(p, line)]
    t += int(s[0] + s[-1])

print(t)

