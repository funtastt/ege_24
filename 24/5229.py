line = open('24.txt').readline()

line = line.replace('A', '.').replace('B', '.').replace('X', '.')

indices = [i for i in range(0, len(line)) if line[i] == '.']

m = 0

for i in range(0, len(indices) - 6):
    l = indices[i+6] - indices[i] - 1
    m = max(m, l)

print(m)