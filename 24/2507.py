line = open('24.txt').readline()

k, m = 1, 1
ch = ''

for i in range(1, len(line)):
    prev, curr = line[i-1], line[i]

    if prev == curr:
        k += 1
    else:
        if k > m:
            m = k
            ch = prev
        k = 1
print(ch, m)