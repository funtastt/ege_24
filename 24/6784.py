line = open('24.txt').readline()

k, m = 0, 0
i = 0

while i < len(line) - 3:
    if line[i:i+2] == 'PC':
        k += 2
        i += 2
    elif line[i:i+2] == 'CSGO':
        k += 4
        i += 4
    else:
        k = 0
        i += 1
    m =max(m, k)
print(m)