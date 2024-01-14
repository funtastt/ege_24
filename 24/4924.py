line = open('24.txt').readline()

k, m = 0, 0

i = 0
while i < len(line) - 2:
    if line[i:i+2] == 'ZXY' or line[i:i+2] == 'ZYZ':
        k += 1
        i += 2
    else:
        k = 0
        i += 1
    m = max(m, k)
print(m)
