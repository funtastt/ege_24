lines = [s.strip() for s in open('24.txt').readlines()]

s = ''

for line in lines:
    while (s+'XYZ') in line:
        s += 'XYZ'

m = 0
for start in ('', 'Z', 'YZ'):
    for end in ('', 'X', 'XY'):
        s = start + s + end
        for line in lines:
            if s in line:
                m = max(m, len(s))

print(m)