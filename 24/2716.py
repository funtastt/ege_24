line = open('24.txt').readline()
k, m = 1, 1
for i in range(1, len(line)):
    prev, curr = int(line[i - 1]), int(line[i])
    if (prev + curr) >= 10:
        k += 1
    else:
        k = 1
    m = max(k, m)
print(m)
