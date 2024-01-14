line = open('24.txt').readline()

flags = [0] * len(line)

for i in range(0, len(line) - 3):
    if line[i:i + 3] in {'AFC', 'ACF', 'FAC', 'FCA', 'CAF', 'CFA'}:
        flags[i:i + 3] = [1] * 3

k, m = 0, 0
for ch in flags:
    if ch == 0:
        k += 1
    else:
        k = 0
    m = max(k, m)
print(m)
