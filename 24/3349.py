line = open('24.txt').readline()
indices = []
m = 0

for i in range(1, len(line) - 1):
    if line[i-1] > line[i] < line[i+1]:
        indices.append(i)

for i in range(1, len(line)):
    m = max(m, indices[i] - indices[i - 1])

print(m)
