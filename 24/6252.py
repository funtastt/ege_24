line = open('24.txt').readline()

d = [0] * len(line)
m = 0

for i in range(2, len(line)):
    if line[i-2] in 'CDF' and line[i] in 'AO':
        d[i] = d[i-3] + 1

    m = max(m, d[i])
print(m)