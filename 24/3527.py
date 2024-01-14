line = open('24.txt').readline()

k, m = 0, len(line)

for ch in line:
    if ch == 'D':
        k += 1
    else:
        if k > 0:
            m = min(k, m)
            k = 0

print(m)