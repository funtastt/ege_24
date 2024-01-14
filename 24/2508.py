line = open('24.txt').readline()

k, m = 1, 1
chars = []
for i in range(1, len(line)):
    prev, curr = line[i-1], line[i]

    if prev == curr:
        k += 1
    else:
        if k >= m:
            m = k
            chars += [[prev, k]]
        k = 1
    m = max(k, m)

for ch, count in chars:
    if count == m:
        print(ch, count)

