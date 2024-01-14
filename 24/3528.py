line = open('24.txt').readline()

line = line[line.index('D'):]

k = 1
m = len(line)

for ch in line:
    if ch == 'D':
        if k != 1:
            m = min(m, k + 1)
            k = 1

    else:
        k += 1
print(m)