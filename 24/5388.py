line = open('24.txt').readline()

k, m = 0, 0
i = 0
digits = '0123456789'
while i < len(line) - 2:
    if line[i] in digits and line[i+1] not in digits:
        k += 1
        i += 2
    else:
        k = 0
        i += 1
    m = max(k, m)

print(m)