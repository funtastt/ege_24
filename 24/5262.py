line = open('24.txt').readline()
k, m = 0, 0
i = 0
while i < len(line) - 3:
    if line[i:i+3] in {'ABC', 'BAC','CAB', 'CBA'}:
        k += 1
        i += 2
    else:
        k = 0
        i += 1
    m = max(k, m)

print(m)