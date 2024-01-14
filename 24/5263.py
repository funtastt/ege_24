line = open('24.txt').readline()
k, m = 0, 0
i = 0
while i < len(line) - 4:
    if line[i:i+4] in {'ABEC', 'BDAC','CAFB', 'CFBA'}:
        k += 1
        i += 3
    else:
        k = 0
        i += 1
    m = max(k, m)

print(m)