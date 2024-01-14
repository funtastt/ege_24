line = open('24.txt').readline()
k, m = 0, 0
i = 0
while i < len(line):
    if line[i:i+3] == 'YZZ':
        k += 3
        i += 3
    elif line[i:i+2] in {'XY','YZ'}:
        k += 2
        i += 2
    else:
        k = 0
        i += 1
    m = max(m, k)
print(m)