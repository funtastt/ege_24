line = open('24.txt').readline()

indices = [i for i in range(0, len(line)) if line[i] == 'A']

m = 0

for i in range(0, len(indices) - 6):
    l = indices[i+6] - indices[i] - 1
    m = max(m, l)

print(m)