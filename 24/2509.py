line = open('24.txt').readline()
k, m = 1, 1
for i in range(1, len(line)):
    prev, curr = line[i-1], line[i]
    if prev != curr:
        k += 1
    else:
        k = 1
    m = max(k, m)
print(m)