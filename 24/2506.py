line = open('24.txt').readline()

k, m = 1, 1

for ch in line:
    if ch == 'C':
        k += 1
    else:
        k = 1
    m = max(k,m)

print(m)