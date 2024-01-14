line = open('24.txt').readline()

line = line.replace('KOT', '...')

k, m = 0, 0

for ch in line:
    if ch == '.':
        k += 1
    else:
        k = 0
    m = max(k, m)
print(m // 3)