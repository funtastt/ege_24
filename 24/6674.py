line = open('24.txt').readline()

indices = [i for i in range(len(line)) if line[i] in 'Z']

m = len(line)

for i in range(0, len(indices) - 119):
    m = min(m, indices[i + 119] - indices[i] + 1)

print(m)
