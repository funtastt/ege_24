line = open('24.txt').readline()

s = ''

while (s + 'XYZ') in line:
    s += 'XYZ'
m = 0
for start in 'Z', 'YZ':
    for end in 'X', 'XY':
        new_s = start + s + end
        if new_s in line:
            m = max(m, len(new_s))
print(m)