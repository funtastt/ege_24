line = open('24.txt').readline()

m = len(line)
indices = [-1] * 16

for i in range(len(line)):
    if line[i] in '0123456789ABCDEF':
        indices[int(line[i], 16)] = i
        k = min(indices)
        if k != -1:
            r = i - k + 1
            m = min(m, r)

print(m)