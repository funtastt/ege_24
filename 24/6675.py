line = open('24.txt').readline()

indices = [i for i in range(len(line)) if line[i] in 'Y']

m = 0

for i in range(0, len(indices) - 151):
    m = max(m, indices[i + 151] - indices[i] - 1)

print(m)
