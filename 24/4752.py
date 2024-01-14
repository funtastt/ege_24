line = open('24.txt').readline()

indices = [i for i in range(len(line)) if line[i] in 'AIOUYE']

m = 0

for i in range(0, len(indices) - 8):
    if '.' not in line[indices[i]:indices[i+8]]:
        m = max(m, indices[i+8] - indices[i] - 1)

print(m)