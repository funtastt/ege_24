line = open('24.txt').readline()

words = [w for w in line.split('XYZ') if len(w) > 0]

m = 0

for s in words:
    if s.startswith('XY'):
        s = s[2:]
    elif s.startswith('X'):
        s = s[1:]

    if s.endswith('YZ'):
        s = s[:-2]
    elif s.endswith('Z'):
        s = s[:-1]

    m = max(m, len(s))

print(m)